import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    rects = []
    xs = set()
    for i in range(n):
        x1, y1, x2, y2 = map(int, lines[1+i].split())
        if x1 == x2 or y1 == y2:
            continue
        rects.append((x1, y1, x2, y2))
        xs.add(x1)
        xs.add(x2)

    adds = defaultdict(list)
    rems = defaultdict(list)
    for x1, y1, x2, y2 in rects:
        adds[x1].append((y1, y2))
        rems[x2].append((y1, y2))

    xs = sorted(xs)
    active = []
    area = 0
    for i in range(len(xs) - 1):
        x = xs[i]
        # удаляем интервалы
        for interval in rems.get(x, ()):
            active.remove(interval)
        # добавляем интервалы
        active.extend(adds.get(x, ()))

        if not active:
            continue

        width = xs[i+1] - x

        active.sort()
        height = 0
        curr_left, curr_right = active[0]
        for j in range(1, len(active)):
            left, right = active[j]
            if left <= curr_right:
                if right > curr_right:
                    curr_right = right
            else:
                height += curr_right - curr_left
                curr_left = left
                curr_right = right
        height += curr_right - curr_left
        area += width * height

    return area


if __name__ == "__main__":
    result = main()
    print(result)
