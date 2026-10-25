import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    count = 0
    maximum = -1
    i = 0
    while True:
        num = int(lines[i])
        if num == 0:
            break
        if num > maximum:
            maximum = num
            count = 1
        elif num == maximum:
            count += 1
        i += 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
