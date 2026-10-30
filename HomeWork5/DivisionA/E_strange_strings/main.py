import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    s = lines[0]

    rle = run_length_encoding(s)
    singles = {}
    res = 0
    for now in rle:
        if now[0] not in singles:
            singles[now[0]] = 0
        prev_val = singles[now[0]]
        singles[now[0]] = max(singles[now[0]], now[1])
        res += singles[now[0]] - prev_val

    pairs = {}
    for i in range(len(rle) - 1):
        pair = (rle[i][0], rle[i + 1][0])
        if pair not in pairs:
            pairs[pair] = []
        pairs[pair].append((rle[i][1], rle[i+1][1]))

    for pair in pairs:
        f_len = {}
        for now_len in pairs[pair]:
            if now_len[0] not in f_len:
                f_len[now_len[0]] = 0
            f_len[now_len[0]] = max(now_len[1], f_len[now_len[0]])
        max_second = 0
        for now_first in sorted(f_len.keys(), reverse=True):
            now_max_second = max(max_second, f_len[now_first])
            res += (now_max_second - max_second) * now_first
            max_second = now_max_second

    return res


def run_length_encoding(string: str) -> list[list[str | int]]:
    res = [["#", 0]]
    for char in string:
        if char == res[-1][0]:
            res[-1][1] += 1
        else:
            res.append([char, 1])
    return res[1:]


if __name__ == "__main__":
    result = main()
    print(result)
