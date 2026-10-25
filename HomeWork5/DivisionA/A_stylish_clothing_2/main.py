import sys


def main(lines: list[str] | None = None) -> tuple[int, int, int, int]:

    lines = lines or sys.stdin.read().splitlines()

    ns = []
    arrays = []
    for i in range(4):
        n = int(lines[2*i])
        ns.append(n)
        array = list(map(int, lines[2*i+1].split()))
        arrays.append(array)

    N = len(arrays)

    for array in arrays:
        array.sort()

    ptrs = [0] * N
    look = [arrays[i][ptrs[i]] for i in range(N)]
    min_idx, min_value = argmin(look)
    max_idx, max_value = argmax(look)
    best_style = max_value - min_value
    best_look = tuple(look)
    while all(ptrs[i] < ns[i] for i in range(N)):
        look = [arrays[i][ptrs[i]] for i in range(N)]
        min_idx, min_value = argmin(look)
        max_idx, max_value = argmax(look)
        style = max_value - min_value
        if style < best_style:
            best_style = style
            best_look = tuple(look)
        ptrs[min_idx] += 1

    return best_look


def argmin(array: list[int]) -> tuple[int, int]:
    min_idx = -1
    min_value = 100_001
    for i, value in enumerate(array):
        if value < min_value:
            min_idx = i
            min_value = value
    return min_idx, min_value


def argmax(array: list[int]) -> tuple[int, int]:
    max_idx = -1
    max_value = - 1
    for i, value in enumerate(array):
        if value > max_value:
            max_idx = i
            max_value = value
    return max_idx, max_value


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
