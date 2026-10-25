import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    nums1 = list(map(int, lines[0].split()))
    nums2 = list(map(int, lines[1].split()))

    return len(set(nums1) & set(nums2))


if __name__ == "__main__":
    result = main()
    print(result)
