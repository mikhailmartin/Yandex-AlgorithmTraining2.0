import sys
import heapq


def main(lines: list[str] | None = None) -> tuple[int, ...]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    civs = []
    for i in range(n):
        s, e = map(int, lines[1+i].split())
        civs.append((s, e, i+1))
    civs.sort(key=lambda x: (x[0], x[1]))

    heap = []
    min_intersect = 2 * 10 ** 9 + 1
    res = (0,)
    for s, e, i in civs:
        while heap and heap[0][0] <= s:
            heapq.heappop(heap)

        if heap:
            prev_e, prev_i = heap[0]

            intersect = min(prev_e, e) - s
            if intersect < min_intersect:
                min_intersect = intersect
                res = (prev_i, i)

        heapq.heappush(heap, (e, i))

    return res


if __name__ == "__main__":
    result = main()
    print(*result)
