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


Пример 1:
input:
1
1
2
2
output:
NO

Пример 2:
input:
2
-4
7
1
output:
2
"""
import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    a = int(lines[0].strip())
    b = int(lines[1].strip())
    c = int(lines[2].strip())
    d = int(lines[3].strip())

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


if __name__ == "__main__":
    result = main()
    print(result)
