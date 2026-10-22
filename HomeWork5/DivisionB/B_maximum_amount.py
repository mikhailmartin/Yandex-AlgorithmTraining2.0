"""
Максимальная сумма

Ограничение времени - 3 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой.


Формат ввода:
В первой строке входных данных записано единственное число n (1 ≤ n ≤ 3⋅10^5)
- размер массива.

Во второй строке записано n целых чисел a_i (−10^9 ≤ a_i ≤ 10^9) - сам массив.


Формат вывода:
Выведите одно число - максимальную сумму на отрезке в данном массиве.


Пример 1:
input:
4
1 2 3 4
output:
10

Пример 2:
input:
4
5 4 -10 4
output:
9
"""
import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))

    max_amount = nums[0]
    curr_amount = nums[0]

    for i in range(1, n):
        curr_amount = max(nums[i], curr_amount + nums[i])
        max_amount = max(max_amount, curr_amount)

    return max_amount


if __name__ == "__main__":
    result = main()
    print(result)
