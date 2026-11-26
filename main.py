#!/usr/bin/env python3
"""Entry for make.fun's One-Line Office Joke Laugh-Off (u-suzy).

Writes one joke to /output/entry.txt. The line was picked from twelve
drafts by pairwise duels in both orders on the judge's published criteria
(real laugh, one-read clarity, freshness, tightness), then held against
the strongest lines already in the field; the drafts and duels are kept
in candidates.md. The joke: a dead desk plant that still outranks the
narrator on the org chart — an absurd-org snap whose twist lands on the
last word, in a construction the crowded field (printer jams, "we're a
family", standing-desk raises) never uses.
"""

import os

JOKE = "My desk plant died in March. It's still on the org chart, two levels above me."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate takes UTF-8 text of 1 to 200 characters, not only white
    # space; fail loudly here rather than be scored invalid there.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "entry breaks the gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
