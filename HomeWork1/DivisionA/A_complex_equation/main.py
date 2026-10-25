import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    a = int(lines[0].strip())
    b = int(lines[1].strip())
    c = int(lines[2].strip())
    d = int(lines[3].strip())

    if a == 0 and b == 0:
        return "INF"
    elif a == 0:
        return "NO"
    elif b == 0:
        if d == 0:
            return "NO"
        else:
            return "0"
    else:
        x = -b / a
        if x % 1 == 0:
            if (c * x + d) == 0:
                return "NO"
            else:
                return str(int(x))
        else:
            return "NO"


if __name__ == "__main__":
    result = main()
    print(result)
