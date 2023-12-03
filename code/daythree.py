import sys
from solution import Solution


class DayThree(Solution):

    def __init__(self):
        self._setup('daythree')

    def part_one(self):
        schema = self.input
        schema_splitted = schema.split('\n')
        self.schema = schema_splitted
        self.schema_width = len(schema_splitted[0])
        self.schema_height = len(schema_splitted) - 1
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
            for idx in range(max(st_idx - 1, 0), min(en_idx + 2, self.schema_width + 1)):
                #print(f'({v_idx - 1}, {idx}) : {self.schema[v_idx -1][idx]}')
                if self.schema[v_idx - 1][idx] != '.' and not self.schema[v_idx - 1][idx].isnumeric():
                    return True
        #down
        if v_idx != self.schema_height - 1:
            for idx in range(max(st_idx - 1, 0), min(en_idx + 2, self.schema_width + 1)):
                #print(f'({v_idx + 1}, {idx}) : {self.schema[v_idx +1][idx]}')
                if self.schema[v_idx + 1][idx] != '.' and not self.schema[v_idx + 1][idx].isnumeric():
                    return True
        #left
        #print(f'({v_idx}, {max(st_idx - 1, 0)}) : {self.schema[v_idx][max(st_idx - 1, 0)]}')
        if self.schema[v_idx][max(st_idx - 1, 0)] != '.' and not self.schema[v_idx][max(st_idx - 1, 0)].isnumeric():
            return True
        #right
        #print(f'({v_idx}, {max(en_idx + 1, 0)}) : {self.schema[v_idx][max(en_idx + 1, 0)]}')
        if self.schema[v_idx][min(en_idx + 1, self.schema_width)] != '.' and not self.schema[v_idx][min(en_idx + 1, self.schema_width)].isnumeric():
            return True

        return False



    def part_two(self):
        pass

DayThree().run(sys.argv[1])
