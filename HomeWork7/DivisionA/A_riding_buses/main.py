import sys
from itertools import product


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    route_lengths = []
    routes = []
    for i in range(k):
        l, *route = list(map(int, lines[1+i].split()))
        route_lengths.append(l)
        routes.append(route)

    p = int(lines[1+k])
    res = []
    for j in range(p):
        b, m, *plan = map(int, lines[1+k+1+j].split())

        t = 0
        for c in plan:

            for dt, i in product(range(max(route_lengths)), range(k)):
                route = routes[i]
                length = route_lengths[i]
                if route[(t + dt) % length] == b:
                    b = route[(t + dt + c) % length]
                    t += dt + c + 1
                    break
            else:
                res.append((0, 0))
                break
        else:
            res.append((t-1, b))

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(" ".join(map(str, r)) for r in result))
