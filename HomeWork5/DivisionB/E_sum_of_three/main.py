import sys


def main(lines: list[str] | None = None) -> tuple[int, ...]:

    lines = lines or sys.stdin.read().splitlines()

    s = int(lines[0])
    n_a, a = lines[1].split(" ", 1)
    n_a = int(n_a)
    a = list(map(int, a.split()))
    n_b, b = lines[2].split(" ", 1)
    n_b = int(n_b)
    b = list(map(int, b.split()))
    n_c, c = lines[3].split(" ", 1)
    n_c = int(n_c)
    c = list(map(int, c.split()))

    k = 0
    seen_c = dict()
    for i in range(n_a):
        num_a = a[i]
        if num_a > s - 2:
            continue

        for j in range(n_b):
            num_b = b[j]
            if num_b > s - (num_a + 1):
                continue

            search = s - (num_a + num_b)
            if search in seen_c:
                k = seen_c[search]
                return i, j, k

            while k < n_c:
                num_c = c[k]
                if num_c == search:
                    return i, j, k
                elif num_c not in seen_c:
                    seen_c[num_c] = k
                k += 1

    return (-1,)


if __name__ == "__main__":
    result = main()
    print(*result)
