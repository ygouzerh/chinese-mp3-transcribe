#!/usr/bin/env python3
"""Download all MP3 files from the BLCUP series page."""

import re
import os
import urllib.request
import urllib.parse

SERIES_URL = "http://www.blcup.com/MobileResSeries?rid=1136db02-d271-4287-9843-0daab9a5f9e6"
DOWNLOAD_URL = "http://www.blcup.com/Common/DownRes?doi={rid}"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "mp3")


def get_resource_ids():
    req = urllib.request.Request(SERIES_URL)
    html = urllib.request.urlopen(req).read().decode("utf-8")
    # Extract resource IDs in order
    rids = re.findall(r'MobileResource\?rid=([a-f0-9-]+)', html)
    return rids


def get_filename_from_headers(headers):
    cd = headers.get("Content-Disposition", "")
    match = re.search(r'filename=(.+?)(?:;|$)', cd)
    if match:
        raw = match.group(1).strip().strip('"')
        return urllib.parse.unquote(raw)
    return None


def download_mp3(rid, index, total):
    url = DOWNLOAD_URL.format(rid=rid)
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    filename = get_filename_from_headers(resp.headers)
    if not filename:
        filename = f"resource_{rid}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(filepath):
        print(f"[{index}/{total}] Skipping (already exists): {filename}")
        return
    print(f"[{index}/{total}] Downloading: {filename}")
    with open(filepath, "wb") as f:
        f.write(resp.read())
    print(f"  -> Saved to mp3/{filename}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Fetching series page...")
    rids = get_resource_ids()
    # Deduplicate while preserving order
    seen = set()
    ordered_rids = []
    for rid in rids:
        if rid not in seen:
            seen.add(rid)
            ordered_rids.append(rid)
    total = len(ordered_rids)
    print(f"Found {total} resources to download.\n")
    for i, rid in enumerate(ordered_rids, 1):
        try:
            download_mp3(rid, i, total)
        except Exception as e:
            print(f"  ERROR downloading {rid}: {e}")
    print(f"\nDone! Files saved to mp3/")


if __name__ == "__main__":
    main()
