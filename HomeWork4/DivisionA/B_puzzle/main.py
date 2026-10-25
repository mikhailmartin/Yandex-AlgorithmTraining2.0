import sys
from collections import Counter


def main(lines: list[str] | None = None) -> Counter:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())

    counter = Counter()
    for i in range(n):
        counter.update(lines[1+i])
    for j in range(m):
        counter.subtract(lines[1+n+j])

    return counter


if __name__ == "__main__":
    result = main()
    print("".join(result.elements()))
