import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())

    positions = defaultdict(list)
    s = lines[1]
    for i, char in enumerate(s):
        positions[char].append(i)

    beautiful = defaultdict(list)
    for i in range(k):
        a, b = lines[2+i]
        beautiful[b].append(a)

    counter = defaultdict(int)
    total = 0
    for b in s:
        for a in beautiful[b]:
            total += counter[a]
        counter[b] += 1

    return total


if __name__ == "__main__":
    result = main()
    print(result)
