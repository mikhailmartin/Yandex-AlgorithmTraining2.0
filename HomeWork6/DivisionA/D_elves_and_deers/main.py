import sys


def main(lines: list[str] | None = None) -> list[tuple[int, int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    m, n = map(int, lines[0].split())
    deers = [(int(x), i) for i, x in enumerate(lines[1].split(), 1)]
    elves = [(int(x), i) for i, x in enumerate(lines[2].split(), 1)]

    deers.sort()
    elves.sort()

    def good(cnt: int) -> list[tuple[int, int, int]] | None:
        """Можно ли выбрать cnt оленей и рассадить на них cnt пар эльфов."""
        curr_deer = 0
        ans = []
        for left_elf in range(cnt):
            # Левый эльф — left_elf-й самый спокойный,
            # правый — (cnt - left_elf)-й с конца (самые темпераментные)
            right_elf = n - cnt + left_elf
            # Ищем первого оленя со строптивостью СТРОГО больше темперамента левого
            while curr_deer < m and deers[curr_deer][0] <= elves[left_elf][0]:
                curr_deer += 1
            # Проверяем, что строптивость СТРОГО меньше темперамента правого
            if curr_deer == m or deers[curr_deer][0] >= elves[right_elf][0]:
                return None
            ans.append((deers[curr_deer][1], elves[left_elf][1], elves[right_elf][1]))
            curr_deer += 1
        return ans

    lo = 0
    hi = min(m, n // 2)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if good(mid) is not None:
            lo = mid
        else:
            hi = mid - 1

    return good(lo)


if __name__ == "__main__":
    result = main()
    print(len(result))
    print("\n".join(" ".join(map(str, r)) for r in result))
