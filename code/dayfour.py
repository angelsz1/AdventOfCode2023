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
        self.lines = self.input.split('\n')
        self.lines = [line for line in self.lines if line != '']
        amounts = []
        for line in self.lines:
            hands = line.split(':')[1].split('|')
            hands = [hand.strip() for hand in hands]
            card_numbers = set(hands[0].split(' '))
            scratch_numbers = set(hands[1].split(' '))
            self.size = len(card_numbers) + len(scratch_numbers)
            card_numbers.update(scratch_numbers)
            winning_numbers = self.size - len(card_numbers)
            amounts.append(winning_numbers)
        card_copies = [1 for _ in range(0, len(self.lines))]
        index = 0
        for amount in amounts:
            num_value = card_copies[index]
            for i in range(index + 1, index + amount + 1):
                print(i)
                card_copies[i] += num_value
            index += 1
        return functools.reduce(lambda x, y: x + y, card_copies)



DayFour().run(sys.argv[1])
