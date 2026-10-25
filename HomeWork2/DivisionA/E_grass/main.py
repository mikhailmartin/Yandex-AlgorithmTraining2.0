import sys
from math import isqrt


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    x1, y1, x2, y2 = map(int, lines[0].split())
    x3, y3, r = map(int, lines[1].split())

    left_x = max(x1, x3 - r)
    right_x = min(x2, x3 + r)
    bottom_y = max(y1, y3 - r)
    top_y = min(y2, y3 + r)

    count = 0
    if left_x > right_x or bottom_y > top_y:
        return count

    r_sq = r * r
    for x in range(left_x, right_x+1):
        cathet_a = x - x3
        cathet_b = isqrt(r_sq - cathet_a * cathet_a)
        y_lo = max(bottom_y, y3 - cathet_b)
        y_hi = min(top_y, y3 + cathet_b)
        if y_lo <= y_hi:
            count += y_hi - y_lo + 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
