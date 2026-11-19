import sys
from typing import Self


class TreeNode:
    def __init__(self, value: int, depth: int) -> None:
        self.value = value
        self.left: Self | None = None
        self.right: Self | None = None
        self.depth = depth


class BinarySearchTree:
    def __init__(self) -> None:
        self.tree: TreeNode | None = None

    def add(self, value: int) -> str:
        if self.tree is None:
            self.tree = TreeNode(value, depth=0)
            return "DONE"
        else:
            return self._add(self.tree, value)

    def _add(self, node: TreeNode, value: int) -> str:
        if value < node.value:
            if node.left:
                return self._add(node.left, value)
            else:
                node.left = TreeNode(value, node.depth + 1)
                return "DONE"
        elif value > node.value:
            if node.right:
                return self._add(node.right, value)
            else:
                node.right = TreeNode(value, node.depth + 1)
                return "DONE"
        else:
            return "ALREADY"

    def search(self, value: int) -> str:
        return self._search(self.tree, value)

    def _search(self, node: TreeNode | None, value: int) -> str:
        if node:
            if value < node.value:
                return self._search(node.left, value)
            elif value > node.value:
                return self._search(node.right, value)
            else:
                return "YES"
        else:
            return "NO"

    def print(self) -> list[str]:
        ans = []

        def dfs(node: TreeNode | None):
            if node:
                dfs(node.left)
                ans.append("." * node.depth + str(node.value))
                dfs(node.right)

        dfs(self.tree)

        return ans


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    tree = BinarySearchTree()
    res = []
    for line in lines:
        if line.startswith("ADD"):
            command, n = line.split()
            ans = tree.add(int(n))
            res.append(ans)
        elif line.startswith("SEARCH"):
            command, n = line.split()
            ans = tree.search(int(n))
            res.append(ans)
        else:
            ans = tree.print()
            res.extend(ans)

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
