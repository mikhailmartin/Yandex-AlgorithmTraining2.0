import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + nums[i]

    res = []
    for j in range(m):
        l, r = map(int, lines[2+j].split())
        ans = pref[r] - pref[l-1]
        res.append(ans)

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
