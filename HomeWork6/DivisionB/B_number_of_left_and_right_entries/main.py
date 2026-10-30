import sys


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    m = int(lines[2])
    queries = list(map(int, lines[3].split()))

    arr = [(x, i) for i, x in enumerate(nums)]
    arr.sort()

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid][0] >= q:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def rbs(lo: int, hi : int) -> int:
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if arr[mid][0] <= q:
                lo = mid
            else:
                hi = mid - 1
        return lo

    res = []
    for q in queries:
        left = lbs(lo=0, hi=n)
        right = rbs(lo=-1, hi=n-1)
        if left == n or right == -1:
            res.append((0, 0))
        else:
            l = arr[left][1] + 1
            r = arr[right][1] + 1

            if l > r:
                res.append((0, 0))
            else:
                res.append((l, r))

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join([" ".join(map(str, answer)) for answer in result]))
