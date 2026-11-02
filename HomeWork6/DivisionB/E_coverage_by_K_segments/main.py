import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    nums.sort()
    mn = nums[0]
    mx = nums[-1]

    def check(length: int) -> bool:

        left = 0
        m = 0

        while left < n and m < k:
            bound = nums[left] + length
            m += 1

            lo = left
            hi = n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > bound:
                    hi = mid
                else:
                    lo = mid + 1
            left = lo

        return left == n

    lo = 0
    hi = mx - mn
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    result = main()
    print(result)
