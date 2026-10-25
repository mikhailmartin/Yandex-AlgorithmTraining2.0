import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    r = int(lines[0])
    i = int(lines[1])
    c = int(lines[2])

    if i == 0:
        return 3 if r != 0 else c
    elif i == 1:
        return c
    elif i == 4:
        return 3 if r != 0 else 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    else:
        return i


if __name__ == "__main__":
    result = main()
    print(result)
