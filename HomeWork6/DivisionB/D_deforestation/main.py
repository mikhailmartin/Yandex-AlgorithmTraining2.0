import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    a, k, b, m, x = map(int, lines[0].split())

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            if a * (mid - mid // k) + b * (mid - mid // m) >= x:
                hi = mid
            else:
                lo = mid + 1
        return lo

    return lbs(lo=1, hi=2*x)


if __name__ == "__main__":
    result = main()
    print(result)
