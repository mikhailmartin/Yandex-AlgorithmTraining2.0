import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    l, k = map(int, lines[0].split())
    blocks = list(map(int, lines[1].split()))

    lo = 0
    hi = k - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if blocks[mid] >= l // 2:
            hi = mid
        else:
            lo = mid + 1
    right = blocks[lo]

    lo = 0
    hi = k - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if blocks[mid] <= (l - 1) // 2:
            lo = mid
        else:
            hi = mid - 1
    left = blocks[lo]

    if left == right:
        return [left]
    else:
        return [left, right]


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
