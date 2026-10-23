"""
Сумма трёх

Ограничение времени - 15 секунд
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Даны три массива целых чисел A, B, C и целое число S.

Найдите такие i, j, k, что A_i + B_j + C_k = S.


Формат ввода:
На первой строке число S (1 ≤ S ≤ 10^9). Следующие три строки содержат описание
массивов A, B, C в одинаковом формате: первое число задаёт длину n
соответствующего массива (1 ≤ n ≤ 15_000), затем заданы n целых чисел от 1 до 10^9
— сам массив.


Формат вывода:
Если таких i, j, k не существует, выведите единственное число −1. Иначе выведите
на одной строке три числа — i, j, k. Элементы массивов нумеруются с нуля. Если
ответов несколько, выведите лексикографически минимальный.


Пример 1:
input:
3
2 1 2
2 3 1
2 3 1
output:
0 1 1

Пример 2:
input:
10
1 5
1 4
1 3
output:
-1

Пример 3:
input:
5
4 1 2 3 4
3 5 2 1
4 5 3 2 2
output:
0 1 2
"""
import sys


def main(lines: list[str] | None = None) -> tuple[int, ...]:

    lines = lines or sys.stdin.read().splitlines()

    s = int(lines[0])
    n_a, a = lines[1].split(" ", 1)
    n_a = int(n_a)
    a = list(map(int, a.split()))
    n_b, b = lines[2].split(" ", 1)
    n_b = int(n_b)
    b = list(map(int, b.split()))
    n_c, c = lines[3].split(" ", 1)
    n_c = int(n_c)
    c = list(map(int, c.split()))

    k = 0
    seen_c = dict()
    for i in range(n_a):
        num_a = a[i]
        if num_a > s - 2:
            continue

        for j in range(n_b):
            num_b = b[j]
            if num_b > s - (num_a + 1):
                continue

            search = s - (num_a + num_b)
            if search in seen_c:
                k = seen_c[search]
                return i, j, k

            while k < n_c:
                num_c = c[k]
                if num_c == search:
                    return i, j, k
                elif num_c not in seen_c:
                    seen_c[num_c] = k
                k += 1

    return (-1,)


if __name__ == "__main__":
    result = main()
    print(*result)
