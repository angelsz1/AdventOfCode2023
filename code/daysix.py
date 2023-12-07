from os import set_blocking
import sys
from solution import Solution
from math import floor, ceil


class DaySix(Solution):

    def __init__(self):
        self._setup('daysix')

    def part_one(self):
        self.input = self.input.strip()
        times, distances = self.input.split('\n')
        times = times.split(':')[1].split()
        distances = distances.split(':')[1].split()
        prod = 1
        for i in range(len(times)):
            x1, x2 = self.get_roots(int(times[i]), -int(distances[i]))
            print(x1, x2)
            prod *= abs(x1 - x2) + 1
        return prod

    def get_roots(self, b, c):
        a = -1
        sqr_discriminant = (b**2 - 4*a*c)**0.5
        x1 = (-b + sqr_discriminant)/(2*a)
        x2 = (-b - sqr_discriminant)/(2*a)
        if x1 == ceil(x1):
            return x1 + 1, x2 - 1
        return ceil(x1), floor(x2)

    def part_two(self):
        self.input = self.input.strip()
        time, distance = [int(x.split(':')[1].replace(' ', '')) for x in self.input.split('\n')]
        x1, x2 = self.get_roots(time, -distance)
        return abs(x1 - x2) + 1

DaySix().run(sys.argv[1])
