import sys


def main(lines: list[str] | None = None) -> tuple[list[str], list[int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    result = set(range(1, n+1))

    answers = []
    i = 1
    while lines[i] != "HELP":
        question = set(map(int, lines[i].split()))

        result_yes = result & question
        if 2 * len(result_yes) > len(result):
            result = result_yes
            answers.append("YES")
        else:
            result -= question
            answers.append("NO")

        i += 1

    return answers, list(sorted(result))


if __name__ == "__main__":
    answers, result = main()
    print("\n".join(answers))
    print(" ".join(map(str, result)))
