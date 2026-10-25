import sys
from collections import Counter


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    nums = lines[0].split()

    counter = Counter(nums)
    result = []
    for num, count in counter.items():
        if count == 1:
            result.append(num)

    return result


if __name__ == "__main__":
    result = main()
    print(" ".join(result))
