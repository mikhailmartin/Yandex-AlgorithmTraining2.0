"""
Параллелограмм

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

На уроке геометрии семиклассники Вася и Петя узнали, что такое параллелограмм.
На перемене после урока они стали играть в игру: Петя называл координаты четырёх
точек в произвольном порядке, а Вася должен был ответить, являются ли эти точки
вершинами параллелограмма.

Вася, если честно, не очень понял тему про параллелограммы, и ему требуется
программа, умеющая правильно отвечать на Петины вопросы.

Напомним, что параллелограммом называется четырёхугольник, противоположные
стороны которого равны и параллельны.


Формат ввода:
В первой строке входного файла записано целое число N (1 ≤ N ≤ 10) - количество
заданных Петей вопросов. Каждая из N последующих строк содержит описание четырёх
точек - четыре пары целых чисел X и Y (−100 ≤ X ≤ 100, −100 ≤ Y ≤ 100),
обозначающих координаты точки. Гарантируется, что четыре точки, о которых идёт
речь в одном вопросе, не лежат на одной прямой.


Формат вывода:
Для каждого из вопросов выведите "YES", если четыре заданные точки могут
образовать параллелограмм, и "NO" в противном случае. Ответ на каждый из
запросов должен быть в отдельной строке без кавычек.


Пример
input: 3
input: 1 1 4 2 3 0 2 3
input: 1 1 5 2 2 3 3 0
input: 0 0 5 1 6 3 1 2
output: YES
output: NO
output: YES
"""
import sys
from dataclasses import dataclass
from itertools import permutations
from typing import Self


@dataclass
class ProblemInput:
    n: int
    questions: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline().strip())
        questions = []
        for _ in range(n):
            xa, ya, xb, yb, xc, yc, xd, yd = map(int, sys.stdin.readline().strip().split())
            questions.append((xa, ya, xb, yb, xc, yc, xd, yd))
        return cls(ProblemInput(n, questions))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        questions = []
        for i in range(n):
            xa, ya, xb, yb, xc, yc, xd, yd = map(int, lines[i+1].split())
            questions.append((xa, ya, xb, yb, xc, yc, xd, yd))
        return cls(ProblemInput(n, questions))

    def solve(self) -> list[str]:

        result = []
        for xa, ya, xb, yb, xc, yc, xd, yd in self.data.questions:
            points = [(xa, ya), (xb, yb), (xc, yc), (xd, yd)]
            answer = "NO"
            for p1, p2, p3, p4 in permutations(points):
                if self.middle(p1, p2) == self.middle(p3, p4):
                    answer = "YES"
                    break
            result.append(answer)

        return result

    @staticmethod
    def middle(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[float, float]:
        return p1[0] + p2[0], p1[1] + p2[1]


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(result))


if __name__ == "__main__":
    main()
