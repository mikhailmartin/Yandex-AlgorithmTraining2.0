import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    events = []
    for i in range(n):
        l, r = map(int, lines[1+i].split())
        events.append((l, 0))
        events.append((r, 1))
    events.sort()

    length = 0
    active = 0
    prev = -1
    for x, event_type in events:
        if active:
            length += x - prev

        if event_type:
            active += 1
        else:
            active -= 1

        prev = x

    return length


if __name__ == "__main__":
    result = main()
    print(result)
