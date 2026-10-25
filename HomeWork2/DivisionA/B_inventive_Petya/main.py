import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    x = lines[0]
    z = lines[1]

    i = z.find(x)
    # слова x нет целиком в z
    if i == -1:
        # 1) есть хвост x в начале z
        for j in range(1, len(x)):
            if z.find(x[j:]) == 0:
                return z[len(x) - j:]
        # 2) необходимо z печатать целиком
        else:
            return z
    else:
        # z должен начинаться с хвоста x
        if len(x) <= i:
            return z

        if x[len(x)-i:] != z[:i]:
            return z

        ptr_z = i
        while ptr_z + len(x) <= len(z) and z[ptr_z:ptr_z + len(x)] == x:
            ptr_z += len(x)

        return z[ptr_z:]


if __name__ == "__main__":
    result = main()
    print(result)
