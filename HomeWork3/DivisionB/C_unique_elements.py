"""
Уникальные элементы

Ограничение времени - 3 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Пример 1:
input:
1 2 2 3 3 3
output:
1

Пример 2:
input:
4 3 5 2 5 1 3 5
output:
4 2 1
"""
import sys
from collections import Counter


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    nums = lines[0].split()

    counter = Counter(nums)
    result = []
    for num, count in counter.items():
        if count == 1:
            result.append(num)

    return result


if __name__ == "__main__":
    result = main()
    print(" ".join(result))
