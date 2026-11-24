import sys


class TreeNode:
    def __init__(self, parent=None, is_left=None) -> None:
        self.left = None
        self.right = None
        self.parent = parent
        self.is_left = is_left


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    res = []
    for i in range(n):
        tree = lines[1+i]
        codes = decode(tree)
        res.append(str(len(codes)))
        res.extend(codes)

    return res


def decode(string: str) -> list[str]:

    root = TreeNode()
    curr = root
    for char in string:
        if char == "D":
            if curr.left is None:
                curr.left = TreeNode(curr, True)
                curr = curr.left
            else:
                curr.right = TreeNode(curr, False)
                curr = curr.right
        else:
            while curr.parent is not None and not curr.is_left:
                curr = curr.parent
            if curr.parent is not None:
                curr = curr.parent
                curr.right = TreeNode(curr, False)
                curr = curr.right

    codes = []
    stack = [(root, "")]
    while stack:
        node, code = stack.pop()
        if node.left is None and node.right is None:
            codes.append(code)
        else:
            if node.right is not None:
                stack.append((node.right, code + "1"))
            if node.left is not None:
                stack.append((node.left, code + "0"))

    return codes


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
