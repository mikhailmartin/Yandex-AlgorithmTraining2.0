import sys
sys.set_int_max_str_digits(5000)


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    mod = 10 ** 18 + 9
    fib_mods = {1}
    a, b = 1, 1
    for _ in range(25000):
        a, b = b, (a + b) % mod
        fib_mods.add(b)

    n = int(lines[0])
    res = []
    for i in range(n):
        num = int(lines[1+i])
        res.append("Yes" if num % mod in fib_mods else "No")

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
