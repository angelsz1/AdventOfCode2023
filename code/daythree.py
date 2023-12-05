import sys
from solution import Solution


class DayThree(Solution):

    def __init__(self):
        self._setup('daythree')
        self.schema = self.input.split('\n')
        self.schema_width = len(self.schema[0])
        self.schema_height = len(self.schema) - 1

    def part_one(self):
        self.schema = self.input.split('\n')
        self.schema_width = len(self.schema[0])
        self.schema_height = len(self.schema) - 1
        schema_splitted = self.schema
        num_st_idx = None
        num_en_inx = None
        part_nums_sum = 0
        for v_idx in range(0, self.schema_height):
            in_num = False
            for h_idx in range(0, self.schema_width):
                if not in_num:
                    if schema_splitted[v_idx][h_idx].isnumeric():
                        num_st_idx = h_idx
                        in_num = True
                else:
                    if not schema_splitted[v_idx][h_idx].isnumeric():
                        num_en_inx = h_idx - 1
                        in_num = False
                        part_nums_sum += self.get_addition(v_idx, num_st_idx, num_en_inx)
            if in_num:
                num_en_inx = self.schema_width - 1
                part_nums_sum += self.get_addition(v_idx, num_st_idx, num_en_inx)

        return part_nums_sum

    def get_addition(self, v_idx, st_idx, en_idx):
        num = self.get_num(v_idx, st_idx, en_idx)
        #print(f'checking {num}... ({v_idx}, {st_idx}, {en_idx})')
        doesSum = self.check_surroundings(v_idx, st_idx, en_idx)
        return num if doesSum else 0

    def get_num(self, v_idx, st_idx, en_idx):
        num = ''
        for idx in range(st_idx, en_idx + 1):
            num += self.schema[v_idx][idx]
        return int(num)

    def check_surroundings(self, v_idx, st_idx, en_idx) -> bool:
        #up
        if v_idx != 0:
            for idx in range(max(st_idx - 1, 0), min(en_idx + 2, self.schema_width)):
                #print(f'({v_idx - 1}, {idx}) : {self.schema[v_idx -1][idx]}')
                if self.schema[v_idx - 1][idx] != '.' and not self.schema[v_idx - 1][idx].isnumeric():
                    return True
        #down
        if v_idx != self.schema_height - 1:
            for idx in range(max(st_idx - 1, 0), min(en_idx + 2, self.schema_width)):
                #print(f'({v_idx + 1}, {idx}) : {self.schema[v_idx +1][idx]}')
                if self.schema[v_idx + 1][idx] != '.' and not self.schema[v_idx + 1][idx].isnumeric():
                    return True
        #left
        #print(f'({v_idx}, {max(st_idx - 1, 0)}) : {self.schema[v_idx][max(st_idx - 1, 0)]}')
        if self.schema[v_idx][max(st_idx - 1, 0)] != '.' and not self.schema[v_idx][max(st_idx - 1, 0)].isnumeric():
            return True
        #right
        #print(f'({v_idx}, {max(en_idx + 1, 0)}) : {self.schema[v_idx][max(en_idx + 1, 0)]}')
        if self.schema[v_idx][min(en_idx + 1, self.schema_width - 1)] != '.' and not self.schema[v_idx][min(en_idx + 1, self.schema_width - 1)].isnumeric():
            return True

        return False

    def part_two(self):
        self.schema = self.input.split('\n')
        self.schema_width = len(self.schema[0])
        self.schema_height = len(self.schema) - 1
        self.gears = {}
        num_st_idx = None
        num_en_inx = None
        for v_idx in range(0, self.schema_height):
            in_num = False
            for h_idx in range(0, self.schema_width):
                if not in_num:
                    if self.schema[v_idx][h_idx].isnumeric():
                        num_st_idx = h_idx
                        in_num = True
                else:
                    if not self.schema[v_idx][h_idx].isnumeric():
                        num_en_inx = h_idx - 1
                        in_num = False
                        self.check_for_gears(v_idx, num_st_idx, num_en_inx)
            if in_num:
                num_en_inx = self.schema_width - 1
                self.check_for_gears(v_idx, num_st_idx, num_en_inx)
        return self.get_gear_ratios_sum(self.sanitize_gears(self.gears))

    def sanitize_gears(self, gears):
        values = gears.values()
        return [value for value in values if len(value) == 2]

    def get_gear_ratios_sum(self, gears):
        sum = 0
        for gear in gears:
            print(gear)
            sum += gear[0] * gear[1]
        return sum

    def check_for_gears(self, v_idx, st_idx, en_idx):
        #up
        if v_idx != 0:
            for idx in range(max(st_idx - 1, 0), min(en_idx + 2, self.schema_width)):
                if self.schema[v_idx - 1][idx] == '*':
                    if self.gears.get(f'{v_idx - 1},{idx}'):
                        self.gears[f'{v_idx - 1},{idx}'] += [self.get_num(v_idx, st_idx, en_idx)]
                    else:
                        self.gears[f'{v_idx - 1},{idx}'] = [self.get_num(v_idx, st_idx, en_idx)]
        #down
        if v_idx != self.schema_height - 1:
            for idx in range(max(st_idx - 1, 0), min(en_idx + 2, self.schema_width)):
                if self.schema[v_idx + 1][idx] == '*':
                    if self.gears.get(f'{v_idx + 1},{idx}'):
                        self.gears[f'{v_idx + 1},{idx}'] += [self.get_num(v_idx, st_idx, en_idx)]
                    else:
                        self.gears[f'{v_idx + 1},{idx}'] = [self.get_num(v_idx, st_idx, en_idx)]

        #left
        if self.schema[v_idx][max(st_idx - 1, 0)] == '*':
            if self.gears.get(f'{v_idx},{max(st_idx - 1, 0)}'):
                self.gears[f'{v_idx},{max(st_idx - 1, 0)}'] += [self.get_num(v_idx, st_idx, en_idx)]
            else:
                self.gears[f'{v_idx},{max(st_idx - 1, 0)}'] = [self.get_num(v_idx, st_idx, en_idx)]
        #right
        if self.schema[v_idx][min(en_idx + 1, self.schema_width - 1)] == '*':
            if self.gears.get(f'{v_idx},{min(en_idx + 1, self.schema_width - 1)}'):
                self.gears[f'{v_idx},{min(en_idx + 1, self.schema_width - 1)}'] += [self.get_num(v_idx, st_idx, en_idx)]
            else:
                self.gears[f'{v_idx},{min(en_idx + 1, self.schema_width - 1)}'] = [self.get_num(v_idx, st_idx, en_idx)]



DayThree().run(sys.argv[1])
