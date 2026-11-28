import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    if n == 1:
        return [1]
    parent = [0] * (n + 1)
    childs = [[] for _ in range(n + 1)]
    for i, a in enumerate(map(int, lines[1].split()), 2):
        parent[i] = a
        childs[a].append(i)

    depth = [0] * (n + 1)
    size = [1] * (n + 1)
    sum_depth = [0] * (n + 1)

    order = [1]
    for p in order:
        for c in childs[p]:
            depth[c] = depth[p] + 1
            order.append(c)

    for c in reversed(order):
        sum_depth[c] += depth[c]
        p = parent[c]
        if p:
            size[p] += size[c]
            sum_depth[p] += sum_depth[c]

    res = []
    for i in range(1, n+1):
        res.append(sum_depth[i] - size[i] * (depth[i] - 1))

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
