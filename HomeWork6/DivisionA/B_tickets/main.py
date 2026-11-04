import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    a, b, c, x, k = map(int, lines[0].split())

    if x < k:
        return 0

    max_price = x // k
    if max_price < a or max_price > b:
        return max_price

    lo = a - 1
    hi = max_price
    while lo < hi:
        mid = (lo + hi + 1) // 2
        tickets_cost = mid * k
        tax_cost = (tickets_cost * c) / 100
        if tickets_cost + tax_cost <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo


if __name__ == "__main__":
    result = main()
    print(result)
