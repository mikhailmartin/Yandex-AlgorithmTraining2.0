import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    string = lines[0]

    count = 0
    for par in string:
        if par == "(":
            count += 1
        elif count > 0:
            count -= 1
        else:
            return "NO"

    return "YES" if count == 0 else "NO"


if __name__ == "__main__":
    result = main()
    print(result)
