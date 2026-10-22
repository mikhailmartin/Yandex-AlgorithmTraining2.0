"""
Префиксные суммы

Ограничение времени - 3 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод


Пример:
input:
4 10
1 2 3 4
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
output:
1
3
6
10
2
5
9
3
7
4
"""
import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + nums[i]

    res = []
    for j in range(m):
        l, r = map(int, lines[2+j].split())
        ans = pref[r] - pref[l-1]
        res.append(ans)

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
