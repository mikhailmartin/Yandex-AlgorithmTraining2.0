import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    counter = defaultdict(int)
    for i in range(n):
        d, a = map(int, lines[1+i].split())
        counter[d] += a

    return list(sorted(counter.items()))


if __name__ == "__main__":
    result = main()
    print("\n".join(f"{d} {a}" for d, a in result))
