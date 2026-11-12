import sys
from math import pi


def main(lines: list[str] | None = None) -> float:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    r_min = float("-inf")
    r_max = float("+inf")
    events = []
    for i in range(n):
        r1, r2, phi1, phi2 = map(float, lines[1+i].split())
        r_min = max(r_min, r1)
        r_max = min(r_max, r2)
        events.append((phi1, 0, i))
        events.append((phi2, 1, i))
    events.sort()

    count = 0
    seen = set()
    for phi, event_type, i in events:
        if event_type == 0:
            count += 1
            seen.add(i)
        elif i in seen:
            count -= 1

    res = 0
    for j in range(2 * n):
        phi, event_type, _ = events[j]
        if event_type == 0:
            count += 1
        else:
            count -= 1

        if count == n:
            if j < 2 * n - 1:
                res += (events[j+1][0] - events[j][0]) * (r_max * r_max - r_min * r_min) / 2
            else:
                res += (events[0][0] - events[2 * n - 1][0] + 2 * pi) * (r_max * r_max - r_min * r_min) / 2

    return res


if __name__ == "__main__":
    result = main()
    print(result)
