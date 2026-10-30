import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    nums.sort()

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= l:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def rbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if nums[mid] <= r:
                lo = mid
            else:
                hi = mid - 1
        return lo

    k = int(lines[2])
    res = []
    for i in range(k):
        l, r = map(int, lines[3+i].split())
        left = lbs(lo=0, hi=n)
        right = rbs(lo=-1, hi=n-1)
        res.append(right - left + 1)

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
