import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    ropes = list(map(int, lines[1].split()))

    sum_ = sum(ropes)
    max_ = max(ropes)
    len1 = max_ - (sum_ - max_)  # взяла один из обрезков
    len2 = sum_  # взяла исходную верёвочку

    return len1 if len1 > 0 else len2


if __name__ == "__main__":
    result = main()
    print(result)
