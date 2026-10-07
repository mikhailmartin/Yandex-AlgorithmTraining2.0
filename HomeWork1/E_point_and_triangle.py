"""
Точка и треугольник

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

На координатной плоскости расположены равнобедренный прямоугольный треугольник
ABC с длиной катета d и точка X. Катеты треугольника лежат на осях координат, а
вершины расположены в точках: A (0,0), B (d,0), C (0,d).

Напишите программу, которая определяет взаимное расположение точки X и
треугольника. Если точка X расположена внутри или на сторонах треугольника,
выведите 0. Если же точка находится вне треугольника, выведите номер ближайшей к
ней вершины.


Формат ввода:
Сначала вводится натуральное число d (не превосходящее 1000), а затем координаты
точки X – два целых числа из диапазона от –1000 до 1000.


Формат вывода:
Если точка лежит внутри, на стороне треугольника или совпадает с одной из
вершин, то выведите число 0. Если точка лежит вне треугольника, то выведите
номер вершины треугольника, к которой она расположена ближе всего (1 – к вершине
A, 2 – к B, 3 – к C). Если точка расположена на одинаковом расстоянии от двух
вершин, выведите ту вершину, номер которой меньше.


Пример 1
input: 5
input: 1 1
output: 0

Пример 2
input: 3
input: -1 -1
output: 1

Пример 3
input: 4
input: 4 4
output: 2

Пример 4
input: 4
input: 2 2
output: 0
"""
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    d: int
    x: int
    y: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        d = int(sys.stdin.readline().strip())
        x, y = map(int, sys.stdin.readline().strip().split())
        return cls(ProblemInput(d, x, y))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        d = int(lines[0])
        x, y = map(int, lines[1].split())
        return cls(ProblemInput(d, x, y))

    def solve(self) -> int:

        d = self.data.d
        x = self.data.x
        y = self.data.y

        if 0 <= x <= d and 0 <= y <= d and x + y <= d:
            return 0

        min_dist = 1001 * 1001
        closest_vertex = -1
        vertexes = ((0, 0), (d, 0), (0, d))
        for i, (xt, yt) in enumerate(vertexes, 1):
            curr_dist = (x - xt) * (x - xt) + (y - yt) * (y - yt)
            if curr_dist < min_dist:
                min_dist = curr_dist
                closest_vertex = i
        return closest_vertex


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
