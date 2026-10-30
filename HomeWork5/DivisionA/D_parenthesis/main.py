import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    pars = lines[0]

    n = len(pars) // 2

    # открывающая скобка раньше закрывающей — всегда корректно
    res = (n + 1) * (2 * n + 1)

    # закрывающая раньше открывающей — считаем возвышенные области
    balance = 0
    length = 0  # текущая длина возвышенной области
    for par in pars:
        balance += 1 if par == "(" else -1

        if balance > 0:
            length += 1
        else:
            res += length * (length + 1) // 2
            length = 0

    return res


if __name__ == "__main__":
    result = main()
    print(result)
