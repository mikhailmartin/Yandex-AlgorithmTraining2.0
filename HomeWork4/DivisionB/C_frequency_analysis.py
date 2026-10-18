"""
Частотный анализ

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
строку. Слова должны быть отсортированы по убыванию их количества появления в
тексте, а при одинаковой частоте появления — в лексикографическом порядке.

Указание:
После того, как вы создадите словарь всех слов, вам захочется отсортировать его
по частоте встречаемости слова. Желаемого можно добиться, если создать список,
элементами которого будут кортежи из двух элементов: частота встречаемости
слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда
стандартная сортировка будет сортировать список кортежей, при этом кортежи
сравниваются по первому элементу, а если они равны — то по второму. Это почти
то, что требуется в задаче.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Пример 1:
input:
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
output:
damme
is
name
van
bond
claude
hi
my
james
jean
what
your

Пример 2:
input:
oh you touch my tralala
mmm my ding ding dong
output:
ding
my
dong
mmm
oh
touch
tralala
you

Пример 3:
input:
ai ai ai ai ai ai ai ai ai ai
output:
ai
"""
import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    counter = defaultdict(int)
    for line in lines:
        words = line.split()
        for word in words:
            counter[word] += 1

    return [item[0] for item in sorted(counter.items(), key=lambda x: (-x[1], x[0]))]


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
