import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    arr.sort()

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2

            cnt = 0
            for a in arr:
                cnt = max(cnt + mid, a)

            if cnt > k:
                hi = mid
            else:
                lo = mid + 1
        return lo

    x = lbs(lo=0, hi=min(arr))
    cnt = 0
    for a in arr:
        cnt = max(cnt + x, a)

    return x - 1 if cnt > k else x


if __name__ == "__main__":
    result = main()
    print(result)
