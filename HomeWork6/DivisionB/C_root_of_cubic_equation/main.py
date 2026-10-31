import sys


def main(lines: list[str] | None = None) -> float:

    lines = lines or sys.stdin.read().splitlines()

    a, b, c, d = map(int, lines[0].split())

    def f(x: float) -> float:
        return ((a * x + b) * x + c) * x + d

    lo = -1.0
    hi = 1.0
    while f(lo) * f(hi) >= 0:
        lo *= 2
        hi *= 2

    for _ in range(100):
        mid = (lo + hi) / 2
        if f(mid) * f(hi) <= 0:
            lo = mid
        else:
            hi = mid

    return lo


if __name__ == "__main__":
    result = main()
    print(result)
