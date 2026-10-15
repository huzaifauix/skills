#!/usr/bin/env python3
"""Brand-name helper: combine word lists into candidates, and bulk-check availability.

Standard library only. Two subcommands:

  combine  Build candidate names from modifier and core word lists.
      python3 names.py combine --mods mods.txt --cores cores.txt [--max-len 9] [--seen results.json]

  check    Check domains (RDAP) and optionally YouTube handles, with a cache.
      python3 names.py check NAME [NAME ...] | --file names.txt
             [--tlds com,co,io,ai] [--youtube] [--cache results.json] [--workers 4]

Word-list files: one word per line; blank lines and lines starting with # are ignored.

Result meanings:
  free     registry returned 404, so the name is very likely unregistered
           (it can still be reserved or premium-priced at a registrar)
  taken    registry returned a record
  unknown  rate limited, timed out, or an unexpected status; re-run later
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

# RDAP servers per TLD (from the IANA bootstrap file plus registry docs for .co).
RDAP = {
    "com": "https://rdap.verisign.com/com/v1/domain/{}",
    "net": "https://rdap.verisign.com/net/v1/domain/{}",
    "co": "https://rdap.registry.co/co/domain/{}",
    "io": "https://rdap.identitydigital.services/rdap/domain/{}",
    "ai": "https://rdap.identitydigital.services/rdap/domain/{}",
    "app": "https://pubapi.registry.google/rdap/domain/{}",
    "dev": "https://pubapi.registry.google/rdap/domain/{}",
    "xyz": "https://rdap.centralnic.com/xyz/domain/{}",
}
UA = "Mozilla/5.0 (brand-name-finder)"
NONSENSE = "zqxwvplmk83"  # sanity-check label that should never be registered


def read_words(path):
    with open(path) as f:
        return [w.strip().lower() for w in f if w.strip() and not w.lstrip().startswith("#")]


def http_status(url, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None


def lookup(url, tries=3):
    """Return 'free', 'taken' or 'unknown', backing off on rate limits."""
    for attempt in range(tries):
        code = http_status(url)
        if code == 404:
            return "free"
        if code == 200:
            return "taken"
        if code in (429, 503, None):
            time.sleep(2 * (attempt + 1))
            continue
        return "unknown"
    return "unknown"


def check_one(name, tlds, youtube):
    row = {}
    for tld in tlds:
        row[tld] = lookup(RDAP[tld].format(f"{name}.{tld}"))
    if youtube:
        row["youtube"] = lookup(f"https://www.youtube.com/@{name}")
    return name, row


def load_cache(path):
    if path and os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def save_cache(path, cache):
    if path:
        tmp = path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(cache, f, indent=1, sort_keys=True)
        os.replace(tmp, path)


def cmd_check(a):
    tlds = [t.strip().lstrip(".").lower() for t in a.tlds.split(",") if t.strip()]
    bad = [t for t in tlds if t not in RDAP]
    if bad:
        sys.exit(f"No RDAP server known for: {', '.join(bad)}. Supported: {', '.join(sorted(RDAP))}")

    names = list(a.names)
    if a.file:
        names += read_words(a.file)
    names = list(dict.fromkeys(re.sub(r"[^a-z0-9-]", "", n.lower()) for n in names if n.strip()))

    # Sanity check: a nonsense name must come back free, otherwise every result is suspect.
    _, probe = check_one(NONSENSE, tlds, a.youtube)
    broken = [k for k, v in probe.items() if v != "free"]
    if broken:
        print(f"WARNING: sanity check failed for {', '.join(broken)}; those columns are unreliable.", file=sys.stderr)

    cache = load_cache(a.cache)
    wanted = tlds + (["youtube"] if a.youtube else [])
    todo = [n for n in names if any(cache.get(n, {}).get(k) in (None, "unknown") for k in wanted)]
    print(f"{len(names)} names, {len(names) - len(todo)} already cached, checking {len(todo)}...", file=sys.stderr)

    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = [ex.submit(check_one, n, tlds, a.youtube) for n in todo]
        for i, fut in enumerate(cf.as_completed(futs), 1):
            n, row = fut.result()
            cache.setdefault(n, {}).update(row)
            if i % 20 == 0:
                save_cache(a.cache, cache)
                print(f"  {i}/{len(todo)}", file=sys.stderr)
    save_cache(a.cache, cache)

    # Table: names with a free primary TLD first, then shorter names.
    primary = tlds[0]
    rows = sorted(names, key=lambda n: (cache[n].get(primary) != "free", len(n), n))
    header = ["name", "len"] + wanted
    print("\t".join(header))
    for n in rows:
        print("\t".join([n, str(len(n))] + [cache[n].get(k, "-") for k in wanted]))
    free = sum(cache[n].get(primary) == "free" for n in names)
    print(f"\n{free}/{len(names)} free on .{primary}" + (f" (cache: {a.cache})" if a.cache else ""), file=sys.stderr)


AWKWARD = re.compile(r"(.)\1\1")  # triple letters like "ppp"


def cmd_combine(a):
    mods, cores = read_words(a.mods), read_words(a.cores)
    seen = set(load_cache(a.seen)) if a.seen else set()
    out = []
    for m in mods:
        for c in cores:
            if m == c:
                continue
            for name in (m + c, c + m):
                # Drop names where the join doubles a letter ("boldd" + "deck") - hard to say and spell.
                if len(name) > a.max_len or AWKWARD.search(name):
                    continue
                if not a.allow_double and (m + c == name and m[-1] == c[0] or c + m == name and c[-1] == m[0]):
                    continue
                if name not in seen:
                    out.append(name)
    for n in sorted(dict.fromkeys(out), key=lambda n: (len(n), n)):
        print(n)
    print(f"{len(set(out))} candidates", file=sys.stderr)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check", help="check domain / YouTube availability")
    c.add_argument("names", nargs="*")
    c.add_argument("--file")
    c.add_argument("--tlds", default="com")
    c.add_argument("--youtube", action="store_true")
    c.add_argument("--cache", default="name-checks.json")
    c.add_argument("--workers", type=int, default=4)
    c.set_defaults(fn=cmd_check)

    b = sub.add_parser("combine", help="build modifier+core candidates")
    b.add_argument("--mods", required=True)
    b.add_argument("--cores", required=True)
    b.add_argument("--max-len", type=int, default=9)
    b.add_argument("--seen", help="cache file; names already checked are skipped")
    b.add_argument("--allow-double", action="store_true", help="keep joins that double a letter")
    b.set_defaults(fn=cmd_combine)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
