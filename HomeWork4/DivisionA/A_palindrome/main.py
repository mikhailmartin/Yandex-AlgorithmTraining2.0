import sys
from collections import Counter


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    letters = list(lines[1])

    counter = Counter(letters)
    order = sorted(counter)
    res = []
    center = None
    for letter in order:
        pair_num, rem = divmod(counter[letter], 2)
        if not center and rem == 1:
            center = letter
        if pair_num > 0:
            res.extend([letter] * pair_num)

    if center:
        res = res + [center] + list(reversed(res))
    else:
        res = res + list(reversed(res))

    return "".join(res)


if __name__ == "__main__":
    result = main()
    print(result)
