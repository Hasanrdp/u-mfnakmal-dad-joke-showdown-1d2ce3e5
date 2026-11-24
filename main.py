#!/usr/bin/env python3
"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt.

The program writes a single original dad joke (92 characters, well inside
the 1-200 character gate) and nothing else. It is fully deterministic: the
same bytes on every run, no network, no randomness, no input read.
"""

import os

JOKE = "I told my wife I was going to start a band called The Leftovers. We only play reheated hits."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    joke = JOKE
    if not joke.strip():
        raise SystemExit("joke must not be blank")
    if len(joke) > MAX_CHARS:
        raise SystemExit(f"joke is {len(joke)} chars, over the {MAX_CHARS} cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
