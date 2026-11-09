import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    events = []
    for i in range(n):
        time, load = map(int, lines[1+i].split())
        events.append((time, 1))
        events.append((time + load, -1))
    events.sort()

    count = 0
    max_count = 0
    for _, event_type in events:
        count += event_type
        max_count = max(max_count, count)

    return max_count


if __name__ == "__main__":
    result = main()
    print(result)
