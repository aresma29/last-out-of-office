"""Print the barista out-of-office line stored in entry.txt."""
from pathlib import Path

line = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
print(line)
