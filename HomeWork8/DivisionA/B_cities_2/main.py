import sys
from collections import defaultdict, deque


def main(lines: list[str] | None = None) -> tuple[int, ...]:
    lines = lines or sys.stdin.read().splitlines()
    n = int(lines[0])
    mapping = defaultdict(list)
    for i in range(1, n):
        a, b = map(int, lines[i].split())
        mapping[a].append(b)
        mapping[b].append(a)

    # обход + размеры поддеревьев
    parent = [0] * (n + 1)
    size = [1] * (n + 1)
    order = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for w in mapping[v]:
            if not seen[w]:
                seen[w] = True
                parent[w] = v
                order.append(w)
    for v in reversed(order):
        if parent[v]:
            size[parent[v]] += size[v]

    # центроиды: все компоненты <= N/2
    centroids = []
    for v in range(1, n + 1):
        biggest = n - size[v]
        for w in mapping[v]:
            if w != parent[v]:
                if size[w] > biggest:
                    biggest = size[w]
        if biggest * 2 <= n:
            centroids.append(v)

    # сумма расстояний BFS из каждого центроида
    def total(src: int) -> int:
        dist = [-1] * (n + 1)
        dist[src] = 0
        q = deque([src])
        s = 0
        while q:
            v = q.popleft()
            s += dist[v]
            for w in mapping[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    q.append(w)
        return s

    sums = {c: total(c) for c in centroids}
    best = min(sums.values())
    centers = [c for c in centroids if sums[c] == best]

    return best, len(centers), *centers


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
