import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    segments = []
    for i in range(n):
        a, b = map(int, lines[1+i].split())
        segments.append((a, b, i+1))
    segments.sort(key=lambda s: (s[0], -s[1]))

    parent = [0] * (n + 1)
    stack = []
    for a, b, i in segments:
        while stack and stack[-1][0] < b:
            stack.pop()

        if stack:
            parent[i] = stack[-1][1]
        stack.append((b, i))

    return parent[1:]


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
