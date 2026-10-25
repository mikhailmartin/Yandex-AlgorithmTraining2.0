import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    k = int(lines[0])
    piles = []
    for i in range(k):
        a, n = map(int, lines[1+i].split())
        piles.append([a, n])

        if k == 1 and n == 1:
            return [a]

    left = 0
    right = k - 1

    # Инициализация A (самая левая) и B (вторая слева)
    A = piles[left][0]
    piles[left][1] -= 1
    B = 0
    if piles[left][1] > 0:
        B = A
        piles[left][1] -= 1
    else:
        if left < right:
            left += 1
            B = piles[left][0]
            piles[left][1] -= 1
        else:
            B = A
            A = 0

    if piles[left][1] == 0 and left < right:
        left += 1

    # Инициализация D (самая правая) и C (предпоследняя)
    D = piles[right][0]
    piles[right][1] -= 1
    C = 0
    if piles[right][1] > 0:
        C = D
        piles[right][1] -= 1
    else:
        if left < right:
            right -= 1
            C = piles[right][0]
            piles[right][1] -= 1
        else:
            C = D
            D = 0

    if piles[right][1] == 0 and left < right:
        right -= 1

    while True:
        if A != 0 and B != 0 and C != 0 and D != 0:
            count = A if A < D else D
            A -= count
            B += count
            C += count
            D -= count
            if A == 0:
                if piles[left][1] > 0:
                    piles[left][1] -= 1
                    A = B
                    B = piles[left][0]
                    if piles[left][1] == 0 and left < right:
                        left += 1
                else:
                    if left < right:
                        left += 1
                        piles[left][1] -= 1
                        A = B
                        B = piles[left][0]
                        if piles[left][1] == 0 and left < right:
                            left += 1
            if D == 0:
                if piles[right][1] > 0:
                    piles[right][1] -= 1
                    D = C
                    C = piles[right][0]
                    if piles[right][1] == 0 and left < right:
                        right -= 1
                else:
                    if left < right:
                        right -= 1
                        piles[right][1] -= 1
                        D = C
                        C = piles[right][0]
                        if piles[right][1] == 0 and left < right:
                            right -= 1
        elif A == 0 and D == 0:
            return [B, C]
        elif A == 0:
            count = B if B < D else D
            B -= count
            C += count * 2
            D -= count
            if B == 0 and D == 0:
                return [C]
            if B == 0:
                return [C, D]
            else:
                return [B, C]
        elif D == 0:
            count = A if A < C else C
            A -= count
            B += count * 2
            C -= count
            if A == 0 and C == 0:
                return [B]
            if A == 0:
                return [B, C]
            else:
                return [A, B]
        elif B == 0:
            return [C]
        elif C == 0:
            return [B]


if __name__ == "__main__":
    result = main()
    print(len(result))
    print(*result)
