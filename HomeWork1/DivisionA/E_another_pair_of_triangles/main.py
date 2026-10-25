import sys


def main(lines: list[str] | None = None) -> tuple[tuple[int, int, int], tuple[int, int, int]] | int:

    lines = lines or sys.stdin.read().splitlines()

    p = int(lines[0])

    # не существует только такого
    if p == 4:
        return -1

    # треугольник с наибольшей площадью
    n, m = divmod(p, 3)
    if m == 0:
        a, b, c = n, n, n
    elif m == 1:
        a, b, c = n+1, n, n
    else:  # m == 2
        a, b, c = n+1, n+1, n

    # треугольник с наименьшей площадью
    n, m = divmod(p, 2)
    if m == 0:
        d, e, f = n-1, n-1, 2
    else:  # m == 1
        d, e, f = n, n, 1

    return (a, b, c), (d, e, f)


if __name__ == "__main__":
    result = main()
    if result == -1:
        print(result)
    else:
        print(*result[0])
        print(*result[1])
