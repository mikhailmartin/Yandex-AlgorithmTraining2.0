"""
Interactor

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Лена руководит разработкой тестирующей системы, в которой реализованы
интерактивные задачи.

До завершения очередной стадии проекта осталось написать модуль, определяющий
итоговый вердикт системы для интерактивной задачи. Итоговый вердикт определяется
из кода завершения задачи, вердикта интерактора и вердикта чекера по следующим
правилам:
- Вердикт чекера и вердикт интерактора — это целые числа от 0 до 7 включительно.
- Код завершения задачи — это целое число от -128 до 127 включительно.
- Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если
  программа завершилась с ненулевым кодом, и вердикту чекера в противном случае.
- Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера.
- Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если
  программа завершилась с ненулевым кодом, и 4 в противном случае.
- Если интерактор выдал вердикт 6, итоговый вердикт равен 0.
- Если интерактор выдал вердикт 7, итоговый вердикт равен 1.
- В остальных случаях итоговый вердикт равен вердикту интерактора.
Ваша задача — реализовать этот модуль.


Формат ввода:
Входной файл состоит из трёх строк. В первой задано целое число r (−128 ≤ r ≤ 127)
— код завершения задачи, во второй — целое число i (0 ≤ i ≤ 7) — вердикт
интерактора, в третьей — целое число c (0 ≤ c ≤ 7) — вердикт чекера.


Формат вывода:
Выведите одно целое число от 0 до 7 включительно — итоговый вердикт системы.


Пример 1
input: 0
input: 0
input: 0
output: 0

Пример 2
input: -1
input: 0
input: 1
output: 3

Пример 3
input: 42
input: 1
input: 6
output: 6

Пример 4
input: 44
input: 7
input: 4
output: 1

Пример 5
input: 1
input: 4
input: 0
output: 3

Пример 6
input: -3
input: 2
input: 4
output: 2
"""
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    r: int
    i: int
    c: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        r = int(sys.stdin.readline().strip())
        i = int(sys.stdin.readline().strip())
        c = int(sys.stdin.readline().strip())
        return cls(ProblemInput(r, i, c))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        r = int(lines[0])
        i = int(lines[1])
        c = int(lines[2])
        return cls(ProblemInput(r, i, c))

    def solve(self) -> int:

        r = self.data.r
        i = self.data.i
        c = self.data.c

        if i == 0:
            return 3 if r != 0 else c
        elif i == 1:
            return c
        elif i == 4:
            return 3 if r != 0 else 4
        elif i == 6:
            return 0
        elif i == 7:
            return 1
        else:
            return i


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
