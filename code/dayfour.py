import sys
import functools
from solution import Solution


class DayFour(Solution):

    def __init__(self):
        self._setup('dayfour')
        self.total_size = 36

    def parse_card(self, line):
        hands = line.split(':')[1].split('|')
        return [set(hands[0].split(' ')), set(hands[1].split(' '))]

    def part_one(self):
        self.lines = self.input.split('\n')
        self.lines = [line for line in self.lines if line != '']
        self.cards = [self.parse_card(line) for line in self.lines]
        self.values = self.calculate_points()
        return functools.reduce(lambda x, y: x + y, self.values)

    def calculate_points(self):
        points = []
        for card in self.cards:
            card[0].update(card[1])
            winning_numbers = self.total_size - len(card[0])
            if winning_numbers != 0:
                points.append(2 ** (self.total_size - len(card[0]) - 1))
        return points

    def part_two(self):
        pass

DayFour().run(sys.argv[1])
