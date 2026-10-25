import sys
from collections import defaultdict


def main(lines: list[str] | None = None) -> list[tuple[str, int]]:

    lines = lines or sys.stdin.read().splitlines()

    order = []
    votes_of = defaultdict(int)
    total_votes = 0
    total_seats = 450
    for line in lines:
        party, votes_str = line.rsplit(" ", 1)
        order.append(party)
        votes = int(votes_str)
        votes_of[party] += votes
        total_votes += votes

    seats_of = dict()
    remainder_of = dict()
    empty_seats = total_seats
    for party, votes in votes_of.items():
        seats, remainder = divmod(votes * total_seats, total_votes)
        seats_of[party] = seats
        empty_seats -= seats
        remainder_of[party] = remainder

    for party, remainder in sorted(remainder_of.items(), key=lambda x: -x[1]):
        if empty_seats:
            seats_of[party] += 1
            empty_seats -= 1
        else:
            break

    return [(party, seats_of[party]) for party in order]


if __name__ == "__main__":
    result = main()
    print("\n".join(f"{party} {seats}" for party, seats in result))
