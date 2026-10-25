import sys


def main(lines: list[str] | None = None) -> tuple[int, int, set[tuple[int, int]]]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    graph = set()
    for k in range(m):
        i, j = map(int, lines[1+k].split())
        if i < j:
            graph.add((i, j))
        elif j < i:
            graph.add((j, i))

    return n, len(graph), graph


if __name__ == "__main__":
    n, m, graph = main()
    print(f"{n} {m}")
    print("\n".join(f"{i} {j}" for i, j in graph))
