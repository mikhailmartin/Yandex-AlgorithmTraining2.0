import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, i, j = map(int, lines[0].split())

    a = (n + j - i) % n
    b = (n + i - j) % n

    return min(a, b) - 1


if __name__ == "__main__":
    result = main()
    print(result)
