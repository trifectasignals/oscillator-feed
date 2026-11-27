#!/usr/bin/env python3
"""Read the Trifecta Oscillator feed and print the current reading.

The Trifecta Oscillator is a market-breadth oscillator published by
Trifecta Signals after each U.S. market close. The feed is free to
read and display with attribution — see the repository README for
terms.

Feed: https://trifectasignals.com/oscillator.json
Page: https://trifectasignals.com/oscillator

Standard library only. Run:  python3 oscillator.py
"""

import http.client
import json
import urllib.request

FEED_URL = "https://trifectasignals.com/oscillator.json"


def fetch_feed(url: str, attempts: int = 3) -> dict:
    """Fetch and parse the feed JSON, retrying truncated transfers."""
    last_error = None
    for _ in range(attempts):
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "oscillator-example", "Accept-Encoding": "identity"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (http.client.IncompleteRead, json.JSONDecodeError) as e:
            last_error = e
    raise RuntimeError(f"Could not read the feed after {attempts} attempts") from last_error


def main() -> None:
    feed = fetch_feed(FEED_URL)

    print(f"{feed['gauge']} — as of {feed['asOf']} ({feed['basis']})")
    print(f"Value: {feed['value']:.2f}  Zone: {feed['zone']}")
    print(
        f"Previous close ({feed['prevDate']}): {feed['prevValue']:.2f} "
        f"({feed['prevZone']})  Change: {feed['change']:+.2f}"
    )
    if feed.get("episodeDay"):
        print(
            f"Oversold episode: day {feed['episodeDay']} "
            f"(began {feed['firstOversold']})"
        )


if __name__ == "__main__":
    main()
