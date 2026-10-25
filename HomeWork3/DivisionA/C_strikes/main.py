import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())

    strikes = set()
    for i in range(k):
        a, b = map(int, lines[1+i].split())
        for j in range(a, n+1, b):
            if (j % 7) != 6 and (j % 7) != 0:
                strikes.add(j)

    return len(strikes)


if __name__ == "__main__":
    result = main()
    print(result)
