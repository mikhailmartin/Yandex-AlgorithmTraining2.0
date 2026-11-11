import sys
from bisect import bisect_left, bisect_right


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    arr.sort()

    res = []
    for i in range(m):
        l, r = map(int, lines[2+i].split())
        res.append(bisect_right(arr, r) - bisect_left(arr, l))

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
