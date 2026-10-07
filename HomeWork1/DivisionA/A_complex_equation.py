"""
Сложное уравнение

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Решить в целых числах уравнение: (ax + b) / (cx + d) = 0


Формат ввода:
Вводятся 4 числа: a, b, c, d; c и d не равны нулю одновременно.


Формат вывода:
Необходимо вывести все решения, если их число конечно, “NO” (без кавычек), если
решений нет, и “INF” (без кавычек), если решений бесконечно много.


Пример 1
input: 1
input: 1
input: 2
input: 2
output: NO

Пример 2
input: 2
input: -4
input: 7
input: 1
output: 2
"""
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    a: int
    b: int
    c: int
    d: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        a = int(sys.stdin.readline().strip())
        b = int(sys.stdin.readline().strip())
        c = int(sys.stdin.readline().strip())
        d = int(sys.stdin.readline().strip())
        return cls(ProblemInput(a, b, c, d))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        a = int(lines[0])
        b = int(lines[1])
        c = int(lines[2])
        d = int(lines[3])
        return cls(ProblemInput(a, b, c, d))

    def solve(self) -> str:

        a = self.data.a
        b = self.data.b
        c = self.data.c
        d = self.data.d

        if a == 0 and b == 0:
            return "INF"
        elif a == 0:
            return "NO"
        elif b == 0:
            if d == 0:
                return "NO"
            else:
                return "0"
        else:
            x = -b / a
            if x % 1 == 0:
                if (c * x + d) == 0:
                    return "NO"
                else:
                    return str(int(x))
            else:
                return "NO"


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
