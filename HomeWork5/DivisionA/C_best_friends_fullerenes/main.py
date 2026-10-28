import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    if n < 3:
        return 0
    nums = list(map(int, lines[1].split()))
    num2s = [x * x for x in nums]

    count = 0
    for i in range(n-2):
        a = nums[i]
        a2 = num2s[i]

        left = i + 2
        right = i + 2
        for j in range(i+1, n-1):
            b = nums[j]
            b2 = num2s[j]

            left = max(left, j + 1)
            right = max(right, j + 1)

            sum = a + b
            sum2 = a2 + b2

            while left < n and num2s[left] <= sum2:
                left += 1

            while right < n and nums[right] < sum:
                right += 1

            count += max(0, right - left)

    return count


if __name__ == "__main__":
    result = main()
    print(result)
