import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    perimeter = 0
    seen = set()
    for i in range(n):
        x, y = map(int, lines[i+1].split())
        adder = 4
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if ((x + dx), (y + dy)) in seen:
                adder -= 2
        perimeter += adder
        seen.add((x, y))

    return perimeter


if __name__ == "__main__":
    result = main()
    print(result)
