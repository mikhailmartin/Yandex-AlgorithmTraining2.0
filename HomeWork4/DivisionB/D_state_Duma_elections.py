"""
Выборы Государственной Думы

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Статья 83 закона “О выборах депутатов Государственной Думы Федерального
Собрания Российской Федерации” определяет следующий алгоритм пропорционального
распределения мест в парламенте.

Необходимо распределить 450 мест между партиями, участвовавших в выборах.
Сначала подсчитывается сумма голосов избирателей, поданных за каждую партию и
подсчитывается сумма голосов, поданных за все партии. Эта сумма делится на 450,
получается величина, называемая “первое избирательное частное” (его смысл - это
количество голосов избирателей, которое необходимо набрать для получения одного
места в парламенте). Далее каждая партия получает столько мест в парламенте,
чему равна целая часть от деления числа голосов за данную партию на первое
избирательное частное. Если после первого раунда распределения мест сумма
количества мест, отданных партиям, меньше 450, то оставшиеся места передаются
по одному партиям, в порядке убывания дробной части частного от деления числа
голосов за данную партию на первое избирательное частное. Если же для двух
партий эти дробные части равны, то преимущество отдаётся той партии, которая
получила большее число голосов.


Формат ввода:
На вход программе подаётся список партий, участвовавших в выборах. Каждая
строка входного файла содержит название партии (строка, возможно, содержащая
пробелы), затем, через пробел, количество голосов, полученных данной партией –
число, не превосходящее 10⁸.


Формат вывода:
Программа должна вывести названия всех партий и количество голосов в
парламенте, полученных данной партией. Названия необходимо выводить в том же
порядке, в котором они шли во входных данных.


Пример 1:
input:
Party One 100000
Party Two 200000
Party Three 400000
output:
Party One 64
Party Two 129
Party Three 257

Пример 2:
input:
Party number one 100
Partytwo 100
output:
Party number one 225
Partytwo 225

Пример 3:
input:
Party number one 449
Partytwo 1
output:
Party number one 449
Partytwo 1
"""
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
