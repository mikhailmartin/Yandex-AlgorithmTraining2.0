import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> list[tuple[str, int]]:

    lines = lines or sys.stdin.read().splitlines()

    counter = defaultdict(int)
    for line in lines:
        surname, count = line.split()
        counter[surname] += int(count)

    return list(sorted(counter.items()))


if __name__ == "__main__":
    result = main()
    print("\n".join(f"{surname} {count}" for surname, count in result))
