import sys


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    nums = map(int, lines[0].split())

    result = []
    seen = set()
    for num in nums:
        result.append("YES" if num in seen else "NO")
        seen.add(num)

    return result


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
