import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    counter = defaultdict(int)
    for line in lines:
        words = line.split()
        for word in words:
            counter[word] += 1

    return [item[0] for item in sorted(counter.items(), key=lambda x: (-x[1], x[0]))]


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
