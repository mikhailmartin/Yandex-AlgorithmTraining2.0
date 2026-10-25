import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    buildings = lines[0].split()
    n = len(buildings)

    # ищем левый магазин
    left_store = 0
    while left_store < n and buildings[left_store] != "2":
        left_store += 1

    # ищем правый магазин
    right_store = 0
    while right_store < n and buildings[right_store] != "2":
        right_store += 1

    # идём по домам
    max_dist = -1
    i = 0
    while i < n:
        if i == right_store:
            left_store = right_store
            right_store += 1
            while right_store < n and buildings[right_store] != "2":
                right_store += 1
            right_store = left_store if right_store == n else right_store
        elif buildings[i] == "1":
            dist = min(abs(left_store - i), abs(right_store - i))
            max_dist = max(max_dist, dist)
        i += 1

    return max_dist


if __name__ == "__main__":
    result = main()
    print(result)
