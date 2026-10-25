import sys


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())

    souls = list(range(n+1))
    for i in range(m):
        i, j = map(int, lines[i+1].split())
        souls[i], souls[j] = souls[j], souls[i]

    def swap(a: int, b: int) -> int:
        souls[a], souls[b] = souls[b], souls[a]
        result.append((a, b))
        return souls[b]

    result = []
    for body in range(1, n-1):
        if souls[body] == body:
            continue

        now = body
        while souls[now] != body:
            now = swap(now, n-1)
        now = swap(now, n)
        swap(now, n)
        swap(souls[n-1], n-1)

    if souls[n-1] == n:
        swap(n-1, n)

    return result


if __name__ == "__main__":
    result = main()
    print("\n".join([f"{i} {j}" for i, j in result]))
