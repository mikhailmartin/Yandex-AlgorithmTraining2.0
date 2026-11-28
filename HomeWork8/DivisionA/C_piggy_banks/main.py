import sys


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.height = [0] * n
        self.n_components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.height[root_x] < self.height[root_y]:
            short = root_x
            tall = root_y
        else:
            short = root_y
            tall = root_x
        self.parent[short] = tall
        if self.height[short] == self.height[tall]:
            self.height[tall] += 1
        self.n_components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    keys = []
    for i in range(n):
        key = int(lines[i+1])
        keys.append(key)

    union_find = UnionFind(n)
    for i, key in enumerate(keys):
        union_find.union(i, key - 1)

    return union_find.n_components


if __name__ == "__main__":
    result = main()
    print(result)
