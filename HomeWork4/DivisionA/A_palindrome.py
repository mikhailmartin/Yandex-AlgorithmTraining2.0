"""
Палиндром

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Палиндром - это строка, которая читается одинаково как справа налево, так и
слева направо.

На вход программы поступает набор больших латинских букв (не обязательно
различных). Разрешается переставлять буквы, а также удалять некоторые буквы.
Требуется из данных букв по указанным правилам составить палиндром наибольшей
длины, а если таких палиндромов несколько, то выбрать первый из них в алфавитном
порядке.


Формат ввода:
В первой строке входных данных содержится число N (1 ≤ N ≤ 100_000). Во второй
строке задаётся последовательность из N больших латинских букв (буквы записаны
без пробелов).


Формат вывода:
В единственной строке выходных данных выдайте искомый палиндром.


Пример 1:
input:
3
AAB
output:
ABA

Пример 2:
input:
6
QAZQAZ
output:
AQZZQA

Пример 3:
input:
6
ABCDEF
output:
A
"""
import sys
from collections import Counter


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    letters = list(lines[1])

    counter = Counter(letters)
    order = sorted(counter)
    res = []
    center = None
    for letter in order:
        pair_num, rem = divmod(counter[letter], 2)
        if not center and rem == 1:
            center = letter
        if pair_num > 0:
            res.extend([letter] * pair_num)

    if center:
        res = res + [center] + list(reversed(res))
    else:
        res = res + list(reversed(res))

    return "".join(res)


if __name__ == "__main__":
    result = main()
    print(result)
