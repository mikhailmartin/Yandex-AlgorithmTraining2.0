import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    string = lines[0]

    n = len(string)
    left = 0
    right = n - 1
    count = 0
    while left < right:
        if string[left] != string[right]:
            count += 1
        left += 1
        right -= 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
