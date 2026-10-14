"""
Встречалось ли число раньше

Ограничение времени - 3 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Во входной строке записана последовательность чисел через пробел. Для каждого
числа выведите слово YES (в отдельной строке), если это число ранее встречалось
в последовательности или NO, если не встречалось.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Пример:
input:
1 2 3 2 3 4
output:
NO
NO
NO
YES
YES
NO
"""
import sys


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    nums = map(int, lines[0].split())

    result = []
    seen = set()
    for num in nums:
        result.append("YES" if num in seen else "NO")
        seen.add(num)

    return result


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
