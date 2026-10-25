import sys
from collections import Counter


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    x = lines[0]
    y = lines[1]

    counter_x = Counter(x)
    counter_y = Counter(y)

    res = []
    ord_a = ord("a")
    ptr_x = 0
    ptr_y = 0
    for num in range(26, -1, -1):
        char = chr(ord_a + num)
        count_x = counter_x.get(char, 0)
        count_y = counter_y.get(char, 0)
        n = min(count_x, count_y)
        while n and ptr_x < len(x) and ptr_y < len(y):
            idx_x = x.find(char, ptr_x)
            idx_y = y.find(char, ptr_y)
            if idx_x != -1 and idx_y != -1:
                res.append(char)
                n -= 1
                ptr_x = idx_x + 1
                ptr_y = idx_y + 1
            else:
                n = 0

    return "".join(res)


if __name__ == "__main__":
    result = main()
    print(result)
