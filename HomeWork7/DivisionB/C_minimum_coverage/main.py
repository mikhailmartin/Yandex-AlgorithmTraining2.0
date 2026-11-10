import sys


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    m = int(lines[0])
    segments = []

    i = 1
    while True:
        l, r = map(int, lines[i].split())
        i += 1
        if l == 0 and r == 0:
            break
        if r >= 0 and l <= m:
            segments.append((l, r))
    segments.sort()

    coverage = []
    covered_until = 0
    seg_ptr = 0
    total_segments = len(segments)
    while covered_until < m:
        furthest_reach = -1
        best_segment = None

        while seg_ptr < total_segments and segments[seg_ptr][0] <= covered_until:
            current_left, current_right = segments[seg_ptr]
            if current_right > furthest_reach:
                furthest_reach = current_right
                best_segment = (current_left, current_right)
            seg_ptr += 1

        if best_segment is None or furthest_reach <= covered_until:
            return []

        coverage.append(best_segment)
        covered_until = furthest_reach

    return coverage


if __name__ == "__main__":
    result = main()
    if not result:
        print("No solution")
    else:
        print(len(result))
        for res in result:
            print(*res)
