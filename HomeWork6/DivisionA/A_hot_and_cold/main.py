def main() -> None:

    lo_x = 0
    hi_x = 10 ** 9

    while lo_x != hi_x:
        print(lo_x, 0, flush=True)
        input()

        print(hi_x, 0, flush=True)
        ans = input()

        if ans == "1":
            lo_x = (hi_x + lo_x) // 2 + 1
        else:
            hi_x = (hi_x + lo_x) // 2
    x = lo_x

    lo_y = 0
    hi_y = 10 ** 9
    while lo_y != hi_y:
        print(x, lo_y, flush=True)
        input()

        print(x, hi_y, flush=True)
        ans = input()

        if ans == "1":
            lo_y = (hi_y + lo_y) // 2 + 1
        else:
            hi_y = (hi_y + lo_y) // 2
    y = lo_y

    print("A", x, y, flush=True)


if __name__ == "__main__":
    main()
