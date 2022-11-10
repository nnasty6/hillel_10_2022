from pathlib import Path
from typing import Generator

from pympler import asizeof

LESSON_04_DIR = Path(__file__).parent
ROCKYOU_FILENAME = LESSON_04_DIR / "rockyou.txt"
FILTERED_DATA_FILE = LESSON_04_DIR / "filtered_data.txt"

johns = []


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline().replace("\n", "")

            if not line:
                break

            if pattern in line.lower():
                yield line


filtered_names = filter_lines(ROCKYOU_FILENAME, "john")


def save_filtered_lines(filename: Path, data: Generator):
    with open(filename, "w") as file:
        file.writelines("%s\n" % line for line in data)


save_filtered_lines(FILTERED_DATA_FILE, filtered_names)
line_count = sum(1 for line in open(FILTERED_DATA_FILE))
line_count_rockyou = sum(1 for line1 in open(ROCKYOU_FILENAME))

print(f'Total lines in file "rockyou" -  {line_count_rockyou}')

print(f"Total lines in file with filtered names - {line_count}")

print(f'Size of "rockyou" - {asizeof.asizeof(ROCKYOU_FILENAME)}')

print(f"Size of filtered file - {asizeof.asizeof(FILTERED_DATA_FILE)}")
