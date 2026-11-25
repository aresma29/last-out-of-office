"""Last Out of Office: The AI That Went Barista.

Prints the competition entry stored in entry.txt, byte-for-byte.
Standard library only. No stripping, no reformatting: what is in
entry.txt is exactly what goes to stdout.
"""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
