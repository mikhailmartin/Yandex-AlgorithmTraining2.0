import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    result = set(range(1, n+1))

    i = 1
    while lines[i] != "HELP":
        question = set(map(int, lines[i].split()))
        answer = lines[i+1]
        if answer == "YES":
            result &= question
        else:
            result -= question
        i += 2

    return list(sorted(result))


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
