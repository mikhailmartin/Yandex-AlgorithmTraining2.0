import sys


MAX_VOTES = 10 ** 6
MAX_PRICE = 10 ** 6
INVALID_PRICE = -1


def main(lines: list[str] | None = None) -> tuple[int, int, list[int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    price = [0] * n
    parties = [(0, 0)] * n
    for party in range(n):
        votes, price[party] = map(int, lines[1+party].split())
        parties[party] = (votes, party)

    # сортировка по возрастанию голосов и подсчет суффиксных сумм
    parties.sort()
    suffix_votes = [0] * n
    suffix_votes[-1] = parties[-1][0]
    for pos in range(n - 2, -1, -1):
        suffix_votes[pos] = suffix_votes[pos+1] + parties[pos][0]

    def haircut_gain(cand: int, level: int) -> int:
        # сколько голосов мы получим от стрижки по level
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if parties[mid][0] < level:
                lo = mid + 1
            else:
                hi = mid
        if parties[lo][0] < level:
            return 0
        gain = suffix_votes[lo] - level * (n - lo)
        if parties[cand][0] >= level:
            gain -= (parties[cand][0] - level)
        return gain

    def plan_for(cand: int) -> tuple[int, int, int]:
        # определение количества денег для победы cand-го кандидата
        cand_votes = parties[cand][0]
        lo = 0
        hi = MAX_VOTES
        while lo < hi:
            level = (lo + hi + 1) // 2
            gain = haircut_gain(cand, level)
            if gain + cand_votes > level:
                lo = level
            else:
                hi = level - 1
        gain = haircut_gain(cand, lo)
        spared = max(0, cand_votes + gain - lo - 2)
        return gain - spared, lo, spared

    # перебор подходящих партий
    best_cost = MAX_PRICE + MAX_VOTES * MAX_PRICE + 1
    best_plan = None
    for pos in range(n):
        cand_votes, orig_id = parties[pos]
        if price[orig_id] != INVALID_PRICE:
            cost, level, spared = plan_for(pos)
            if price[orig_id] + cost < best_cost:
                best_cost = price[orig_id] + cost
                best_plan = [pos, cost, level, spared]

    # восстановление ответа
    winner_pos, cost, level, spared = best_plan
    final_votes = [0] * n
    for pos in range(n):
        cand_votes, orig_id = parties[pos]
        if pos == winner_pos:
            final_votes[orig_id] = cand_votes + cost
        elif cand_votes <= level:
            final_votes[orig_id] = cand_votes
        else:
            if spared > 0:
                final_votes[orig_id] = level + 1
                spared -= 1
            else:
                final_votes[orig_id] = level

    return best_cost, parties[winner_pos][1] + 1, final_votes


if __name__ == "__main__":
    best_cost, winner_id, final_votes = main()
    print(best_cost)
    print(winner_id)
    print(*final_votes)
