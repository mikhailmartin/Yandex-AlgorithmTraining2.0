import sys
from itertools import product


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    matrix = []
    for i in range(3):
        matrix.append(lines[i].split())

    x_count = 0
    o_count = 0
    for cx, cy in product(range(3), range(3)):
        char = matrix[cx][cy]
        if char == "1":
            x_count += 1
        elif char == "2":
            o_count += 1

    if x_count < o_count:
        return "NO"
    elif x_count - o_count > 1:
        return "NO"

    win_lines = [
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),

        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),

        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    ]
    x_wins = False
    o_wins = False
    for c1, c2, c3 in win_lines:
        char = matrix[c1[0]][c1[1]]
        if char == "0":
            continue
        if char == matrix[c2[0]][c2[1]] and char == matrix[c3[0]][c3[1]]:
            if char == "1":
                x_wins = True
            else:
                o_wins = True

    if x_wins and o_wins:
        return "NO"
    elif x_wins and x_count == o_count:
        return "NO"
    elif o_wins and x_count > o_count:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    result = main()
    print(result)
