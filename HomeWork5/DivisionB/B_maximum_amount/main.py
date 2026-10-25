import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))

    max_amount = nums[0]
    curr_amount = nums[0]

    for i in range(1, n):
        curr_amount = max(nums[i], curr_amount + nums[i])
        max_amount = max(max_amount, curr_amount)

    return max_amount


if __name__ == "__main__":
    result = main()
    print(result)
