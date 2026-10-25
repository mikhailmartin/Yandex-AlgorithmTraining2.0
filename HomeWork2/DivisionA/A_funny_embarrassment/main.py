import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    return max(nums) - min(nums)


if __name__ == "__main__":
    result = main()
    print(result)
