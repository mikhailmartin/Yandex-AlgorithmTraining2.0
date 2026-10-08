"""
Проверьте правильность ситуации

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Напишите программу, которая по изображению поля для игры в «Крестики-нолики»
определит, могла ли такая ситуация возникнуть в результате игры с соблюдением
всех правил.

Напомним, что игра в «Крестики-нолики» ведётся на поле 3*3. Два игрока ходят по
очереди. Первый ставит крестик, а второй – нолик. Ставить крестик и нолик
разрешается в любую ещё не занятую клетку поля. Когда один из игроков поставит
три своих знака в одной горизонтали, вертикали или диагонали, или когда все
клетки поля окажутся заняты, игра заканчивается.


Формат ввода:
Вводится три строки по три числа в каждой, описывающих игровое поле. Число 0
обозначает пустую клетку, 1 – крестик, 2 – нолик. Числа в строке разделяются
пробелами.


Формат вывода:
Требуется вывести слово YES, если указанная ситуация могла возникнуть в ходе
игры, и NO в противном случае.


Пример 1:
input:
1 1 1
1 1 1
1 1 1
output:
NO

Пример 2:
input:
2 1 1
1 1 2
2 2 1
output:
YES

Пример 3:
input:
1 1 1
2 0 2
0 0 0
output:
YES

Пример 4:
input:
0 0 0
0 1 0
0 0 0
output:
YES
"""
import sys
from itertools import product


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    matrix = []
    for i in range(3):
        matrix.append(lines[i].split())

    x_count = 0
    o_count = 0
    for cx, cy in product(range(3), range(3)):
        char = matrix[cx][cy]
        if char == "1":
            x_count += 1
        elif char == "2":
            o_count += 1

    if x_count < o_count:
        return "NO"
    elif x_count - o_count > 1:
        return "NO"

    win_lines = [
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),

        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),

        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    ]
    x_wins = False
    o_wins = False
    for c1, c2, c3 in win_lines:
        char = matrix[c1[0]][c1[1]]
        if char == "0":
            continue
        if char == matrix[c2[0]][c2[1]] and char == matrix[c3[0]][c3[1]]:
            if char == "1":
                x_wins = True
            else:
                o_wins = True

    if x_wins and o_wins:
        return "NO"
    elif x_wins and x_count == o_count:
        return "NO"
    elif o_wins and x_count > o_count:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    result = main()
    print(result)
