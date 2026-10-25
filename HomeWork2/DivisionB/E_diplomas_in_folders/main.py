import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = lines[0]
    nums = list(map(int, lines[1].split()))

    return sum(nums) - max(nums)


if __name__ == "__main__":
    result = main()
    print(result)
