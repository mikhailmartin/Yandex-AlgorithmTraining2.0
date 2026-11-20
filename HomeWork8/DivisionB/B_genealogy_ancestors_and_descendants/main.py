import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()
    n_lines = len(lines)

    n = int(lines[0])
    parents_of = defaultdict(list)
    for i in range(n - 1):
        child, parent = lines[1+i].split()
        parents_of[child].append(parent)

    def reaches(start: str, target: str) -> bool:
        parents = parents_of.get(start, []).copy()
        while parents:
            parent = parents.pop()
            if parent == target:
                return True
            parents.extend(parents_of.get(parent, []))
        return False

    i = n
    res = []
    while i < n_lines:
        first, second = lines[i].split()

        if reaches(first, second):
            res.append("2")
        elif reaches(second, first):
            res.append("1")
        else:
            res.append("0")

        i += 1

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(result))
