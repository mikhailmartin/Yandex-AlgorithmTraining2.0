import sys
from collections import defaultdict, deque


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    if n == 1:
        return 1

    mapping = defaultdict(list)
    for i in range(1, n):
        a, b = map(int, lines[i].split())
        mapping[a].append(b)
        mapping[b].append(a)

    # ищем лист
    j = 1
    while True:
        if len(mapping[j]) == 1:
            break
        j += 1

    def farthest(src: int) -> tuple[int, int]:
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
        return best, dist[best]

    u, _ = farthest(1)
    _, d = farthest(u)

    return d + 1


if __name__ == "__main__":
    result = main()
    print(result)
