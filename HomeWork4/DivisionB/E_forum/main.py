import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    counter = dict()
    messages = []
    i = 1
    for _ in range(n):
        num = int(lines[i])
        i += 1

        if num == 0:
            topic = lines[i]
            i += 1

            message = lines[i]
            i += 1

            counter[topic] = 1
            messages.append(topic)

        else:
            message = lines[i]
            i += 1

            topic = messages[num-1]

            counter[topic] += 1
            messages.append(topic)

    max_count = 0
    populest_topic = ""
    for topic, count in counter.items():
        if count > max_count:
            max_count = count
            populest_topic = topic

    return populest_topic


if __name__ == "__main__":
    result = main()
    print(result)
