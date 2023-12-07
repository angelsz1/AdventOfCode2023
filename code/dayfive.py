import sys
from solution import Solution


class DayFive(Solution):

    def __init__(self):
        self._setup('dayfive')

    def part_one(self):
        data = [x.split('\n') for x in self.input.split('\n\n')]
        seeds = [int(x) for x in data[0][0].split()[1::]]
        for i in range(1,8):
            map = None
            if i != 7:
                map = self.gen_map(data[i][1::])
            else: 
                map = self.gen_map(data[i][1:-1])
            seeds = [self.get_dest(seed, map) for seed in seeds]
        return min(seeds)

    def get_dest(self, seed, map):
        if not map.get(seed):
            return seed
        return map[seed]

    def gen_map(self, data):
        map = {}
        for cat in data:
            dest_st, orig_st, rang_len = [int(x) for x in cat.split()]
            for i in range(rang_len):
                map[orig_st + i] = dest_st + i
        return map

    def part_two(self):
        pass

DayFive().run(sys.argv[1])
