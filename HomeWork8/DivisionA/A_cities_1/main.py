import sys
from collections import defaultdict, deque


def main(lines: list[str] | None = None) -> tuple[int, ...]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    if n == 1:
        return 0, 1, 1

    mapping = defaultdict(list)
    for i in range(1, n):
        a, b = map(int, lines[i].split())
        mapping[a].append(b)
        mapping[b].append(a)

    def farthest(src: int) -> tuple[int, dict[int, int]]:
        dist = {src: 0}
        deq = deque([src])
        best = src
        while deq:
            v = deq.popleft()
            if dist[v] > dist[best]:
                best = v
            for w in mapping[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    deq.append(w)
        return best, dist

    u, _ = farthest(1)
    v, dist_u = farthest(u)
    _, dist_v = farthest(v)

    radius = (dist_u[v] + 1) // 2
    centers = [w for w in range(1, n + 1) if max(dist_u[w], dist_v[w]) == radius]

    return radius, len(centers), *centers


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
