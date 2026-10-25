import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    d = int(lines[0])
    x, y = map(int, lines[1].split())

    if 0 <= x <= d and 0 <= y <= d and x + y <= d:
        return 0

    min_dist = 1001 * 1001
    closest_vertex = -1
    vertexes = ((0, 0), (d, 0), (0, d))
    for i, (xt, yt) in enumerate(vertexes, 1):
        curr_dist = (x - xt) * (x - xt) + (y - yt) * (y - yt)
        if curr_dist < min_dist:
            min_dist = curr_dist
            closest_vertex = i

    return closest_vertex


if __name__ == "__main__":
    result = main()
    print(result)
