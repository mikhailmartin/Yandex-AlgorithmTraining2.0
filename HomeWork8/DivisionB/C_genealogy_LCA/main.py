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

    i = n
    res = []
    while i < n_lines:
        first, second = lines[i].split()

        first_parents = set()
        stack = [first]
        while stack:
            parent = stack.pop()
            if parent not in first_parents:
                first_parents.add(parent)
                stack.extend(parents_of.get(parent, []))

        second_parents = set()
        stack = [second]
        while stack:
            parent = stack.pop()

            if parent in first_parents:
                res.append(parent)
                break

            if parent not in second_parents:
                second_parents.add(parent)
                stack.extend((parents_of.get(parent, [])))

        i += 1

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
