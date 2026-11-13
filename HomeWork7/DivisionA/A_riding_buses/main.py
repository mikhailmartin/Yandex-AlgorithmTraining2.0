import sys


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    ...

    return


if __name__ == "__main__":
    result = main()
    print(result)
