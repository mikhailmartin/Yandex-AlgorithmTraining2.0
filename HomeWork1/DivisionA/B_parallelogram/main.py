import sys
from itertools import permutations


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    result = []
    for i in range(n):
        xa, ya, xb, yb, xc, yc, xd, yd = map(int, lines[i+1].split())
        points = [(xa, ya), (xb, yb), (xc, yc), (xd, yd)]
        answer = "NO"
        for p1, p2, p3, p4 in permutations(points):
            if p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]:
                answer = "YES"
                break
        result.append(answer)

    return result


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
