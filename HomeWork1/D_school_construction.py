"""
Строительство школы

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

В деревне Интернетовка все дома расположены вдоль одной улицы по одну сторону от
неё. По другую сторону от этой улицы пока ничего нет, но скоро всё будет –
школы, магазины, кинотеатры и т.д.

Для начала в этой деревне решили построить школу. Место для строительства школы
решили выбрать так, чтобы суммарное расстояние, которое проезжают ученики от
своих домов до школы, было минимально.

План деревни можно представить в виде прямой, в некоторых целочисленных точках
которой находятся дома учеников. Школу также разрешается строить только в
целочисленной точке этой прямой (в том числе разрешается строить школу в точке,
где расположен один из домов – ведь школа будет расположена с другой стороны
улицы).

Напишите программу, которая по известным координатам домов учеников поможет
определить координаты места строительства школы.


Формат ввода:
Сначала вводится число N — количество учеников (0 < N < 100_001). Далее идут в
строго возрастающем порядке координаты домов учеников — целые числа, не
превосходящие 2×10^9 по модулю.


Формат вывода:
Выведите одно целое число — координату точки, в которой лучше всего построить
школу. Если ответов несколько, выведите любой из них.


Пример 1
input: 4
input: 1 2 3 4
output: 3

Пример 2
input: 3
input: -1 0 1
output: 0
"""
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    students: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline().strip())
        students = list(map(int, sys.stdin.readline().strip().split()))
        return cls(ProblemInput(n, students))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        students = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, students))

    def solve(self) -> int:
        return self.data.students[self.data.n // 2]


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
