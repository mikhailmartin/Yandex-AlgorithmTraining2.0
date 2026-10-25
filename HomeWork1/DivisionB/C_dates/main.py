import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    x, y, z = map(int, lines[0].split())

    if x == y:
        return 1
    elif x > 12 or y > 12:
        return 1
    else:
        return 0


if __name__ == "__main__":
    result = main()
    print(result)
