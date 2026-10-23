"""
Стильная одежда 2

Ограничение времени - 2 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Глеб обожает шоппинг. Как-то раз он загорелся идеей подобрать себе кепку, майку,
штаны и ботинки так, чтобы выглядеть в них максимально стильно. В понимании
Глеба стильность одежды тем больше, чем меньше разница в цвете элементов его
одежды.

В наличии имеется N_1 кепок, N_2 маек, N_3 штанов и N_4 пар ботинок
(1 ≤ N_i ≤ 100_000). Про каждый элемент одежды известен его цвет (целое число от
1 до 100_000). Комплект одежды — это одна кепка, майка, штаны и одна пара
ботинок. Каждый комплект характеризуется максимальной разницей между любыми
двумя его элементами. Помогите Глебу выбрать максимально стильный комплект, то
есть комплект с минимальной разницей цветов.


Формат ввода:
Для каждого типа одежды i (i = 1, 2, 3, 4) сначала вводится количество N_i
элементов одежды этого типа, далее в следующей строке — последовательность из
N_i целых чисел, описывающих цвета элементов. Все четыре типа подаются на вход
последовательно, начиная с кепок и заканчивая ботинками. Все вводимые числа
целые, положительные и не превосходят 100_000.


Формат вывода:
Выведите четыре целых числа — цвета соответственно для кепки, майки, штанов и
ботинок, которые должен выбрать Глеб из имеющихся для того, чтобы выглядеть
наиболее стильно. Если ответов несколько, выведите любой.


Пример 1:
input:
3
1 2 3
2
1 3
2
3 4
2
2 3
output:
3 3 3 3

Пример 2:
input:
1
5
4
3 6 7 10
4
18 3 9 11
1
20
output:
5 6 9 20
"""
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
