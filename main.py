"""One line roasting the fridge.

Writes the line to /output/entry.txt, where the grader reads it.
Gate for this bounty: 1 to 200 characters, UTF-8, not only whitespace.
The roast finds one specific detail: the hum is loud, the milk still dies —
it is very good at noise and very bad at the one job it was bought for.
"""

from pathlib import Path

LINE = "My fridge hums louder than my neighbour's karaoke and still can't keep the milk from turning into a science experiment."

OUT = Path("/output/entry.txt")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
