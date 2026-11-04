import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, m, r = map(int, lines[0].split())
    mapping = defaultdict(list)
    seen = set()
    for i in range(n):
        participant_id, region, score, winner = map(int, lines[1+i].split())
        if winner:
            seen.add(region)
            m -= 1
        else:
            mapping[region].append(score)

    other_scores = []
    for region, scores in mapping.items():
        if region in seen:
            other_scores.extend(scores)
        else:
            mx = max(scores)
            for score in scores:
                if score != mx:
                    other_scores.append(score)
            m -= 1
    other_scores.sort(reverse=True)

    return other_scores[m] + 1


if __name__ == "__main__":
    result = main()
    print(result)
