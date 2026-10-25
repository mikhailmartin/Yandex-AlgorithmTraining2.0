import sys
from collections import Counter


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    a = lines[0].strip()
    b = lines[1].strip()

    counter_a = Counter(a)
    counter_b = Counter(b)

    res = []
    for digit in range(9, 0, -1):
        digit_str = str(digit)
        count_a = counter_a.get(digit_str, 0)
        count_b = counter_b.get(digit_str, 0)
        res.extend([digit_str] * min(count_a, count_b))

    count_a = counter_a.get("0", 0)
    count_b = counter_b.get("0", 0)
    if res:
        res.extend(["0"] * min(count_a, count_b))
    else:
        res.extend(["0"] * min(count_a, count_b, 1))

    res = "".join(res)

    return res or "-1"


if __name__ == "__main__":
    result = main()
    print(result)
