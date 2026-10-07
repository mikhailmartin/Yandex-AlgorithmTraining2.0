"""
Кольцевая линия метро

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Витя работает недалеко от одной из станций кольцевой линии Московского метро, а
живёт рядом с другой станцией той же линии. Требуется выяснить, мимо какого
наименьшего количества промежуточных станций необходимо проехать Вите по кольцу,
чтобы добраться с работы домой.


Формат ввода:
Станции пронумерованы подряд натуральными числами 1, 2, 3, …, N (1-я станция –
соседняя с N-й), N не превосходит 100.

Вводятся три числа: сначала N – общее количество станций кольцевой линии, а
затем i и j – номера станции, на которой Витя садится, и станции, на которой он
должен выйти. Числа i и j не совпадают. Все числа разделены пробелом.


Формат вывода:
Требуется выдать минимальное количество промежуточных станций (не считая станции
посадки и высадки), которые необходимо проехать Вите.


Пример 1
input: 100 5 6
output: 0

Пример 2
input: 10 1 9
output: 1


Пояснения к примерам:
1) На кольцевой линии 100 станций; проехать с 5-й на 6-ю станцию Витя может
   напрямую, без промежуточных станций
2) На кольцевой линии 10 станций; проехать с 1-й на 9-ю станцию Витя может через
   одну промежуточную, ее номер 10
"""
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    i: int
    j: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, i, j = map(int, sys.stdin.readline().strip().split())
        return cls(ProblemInput(n, i, j))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, i, j = map(int, lines[0].split())
        return cls(ProblemInput(n, i, j))

    def solve(self) -> int:

        n = self.data.n
        i = self.data.i
        j = self.data.j

        a = (n + j - i) % n
        b = (n + i - j) % n

        return min(a, b) - 1


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
