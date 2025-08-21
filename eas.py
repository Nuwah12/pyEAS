#!/usr/bin/env python3
import json, sys
from datetime import datetime, timezone
import time
from typing import List
import requests
import argparse

### global API URL variable
API = "https://api.weather.gov/alerts/active"

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Get real time NWS EAS information."
    )
    
    parser.add_argument(
        "-c", "--config",
        help="Path to the config file (default: config.json)",
        default="config.json"
    )

    return parser.parse_args()

def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def iso(ts):
    if not ts: return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)
    except Exception:
        return None

def fetch_active_for_point(point):
    lat, lon = [x.strip() for x in point.split(",")]
    ### URL
    url = f"{API}?point={lat},{lon}"
    ### GET request
    try:
        # NWS API requires that `User-Agent` be set in the HTTP header
        r = requests.get(url, headers={"User-Agent": "eas-simple/0.1"}, timeout=20)
        r.raise_for_status()
        return r.json().get("features", [])
    except requests.HTTPError as err:
        print(f"HTTP error: {err}")
    except TimeoutError as err:
        print(f"Request timed out: {err}")
    except requests.RequestException as err:
        print(f"Request error: {err}")

    return None

def show(features):
    if not features:
        print("No active alerts for this location.")
        return
    # sort by severity-ish then newest sent
    sev_rank = {"Extreme":0,"Severe":1,"Moderate":2,"Minor":3}
    features.sort(key=lambda f: (
        sev_rank.get(f["properties"].get("severity",""), 9),
        - (iso(f["properties"].get("sent")) or datetime.min.replace(tzinfo=timezone.utc)).timestamp()
    ))
    try:
        while True:
            print(f"Active alerts: {len(features)}\n")
            for i, f in enumerate(features, 1):
                p = f["properties"]
                ev = p.get("event","")
                headline = p.get("headline") or ev
                sev = p.get("severity","")
                urg = p.get("urgency","")
                cer = p.get("certainty","")
                sent = iso(p.get("sent"))
                expires = iso(p.get("expires"))
                area = (p.get("areaDesc") or "")[:200]  # keep short
                desc = (p.get("description") or "").strip().splitlines()[:6]
                print(f"[{i}] {ev} — {headline}")
                print(f"    Severity={sev}  Urgency={urg}  Certainty={cer}")
                if sent:    print(f"    Sent={sent.strftime('%Y-%m-%d %H:%MZ')}")
                if expires: print(f"    Expires={expires.strftime('%Y-%m-%d %H:%MZ')}")
                if area:    print(f"    Areas: {area}{'…' if len(p.get('areaDesc',''))>200 else ''}")
                if desc:
                    print("    Description:")
                    for line in desc:
                        print(f"      {line}")
                print(f"    More: {p.get('url')}\n")
                
                time.sleep(30)
                
    except KeyboardInterrupt:
        print("\n======== Exit ========")
        sys.exit(0)

def main():
    parser = get_parser() # set up cli args
    cfg = load_config(parser.config)# load config file
    point = cfg.get("point") # get the coordinate from config
    if not point:
        print(f"[ERROR] Must provide a `point` value in {parser.config}"); sys.exit(1)
        
    features = fetch_active_for_point(point)
    show(features)

if __name__ == "__main__":
    main()
