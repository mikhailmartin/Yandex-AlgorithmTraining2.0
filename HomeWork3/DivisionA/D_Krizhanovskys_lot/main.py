import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    scores = list(map(int, lines[1].split()))
    nums = list(map(int, lines[2].split()))

    unique = set()
    not_unique = set()
    for num in nums:
        if num in not_unique:
            continue
        elif num in unique:
            unique.remove(num)
            not_unique.add(num)
        else:
            unique.add(num)

    max_count = -1
    res = -1
    for ans in range(1, 102):
        scores_copy = scores.copy()
        nums_copy = nums.copy()
        unique_copy = unique.copy()
        not_unique_copy = not_unique.copy()

        nums_copy.append(ans)

        if ans in not_unique_copy:
            pass
        elif ans in unique_copy:
            unique_copy.remove(ans)
            not_unique_copy.add(ans)
        else:
            unique_copy.add(ans)

        if unique_copy:
            winner = min(unique_copy)

            for i, num in enumerate(nums_copy):
                if num == winner:
                    scores_copy[i] += winner

        count = 0
        for j in range(n - 1):
            if scores_copy[j] < scores_copy[-1]:
                count += 1

        if count > max_count:
            max_count = count
            res = ans

    return res


if __name__ == "__main__":
    result = main()
    print(result)
