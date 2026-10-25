import sys


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    m = int(lines[0])
    witnesses = []
    for i in range(m):
        witness = set(lines[i+1])
        witnesses.append(witness)

    n = int(lines[1+m])
    max_count = 0
    result = []
    for j in range(n):
        candidate = lines[j+m+2]
        candidate_set = set(candidate)

        count = 0
        for witness in witnesses:
            if witness == candidate_set & witness:
                count += 1

        if count == max_count:
            result.append(candidate)
        elif count > max_count:
            max_count = count
            result = [candidate]

    return result


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
