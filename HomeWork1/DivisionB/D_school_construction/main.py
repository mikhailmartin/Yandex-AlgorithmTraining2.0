import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    students = list(map(int, lines[1].split()))

    return students[n // 2]


if __name__ == "__main__":
    result = main()
    print(result)
