from functools import partial
from solution import Solution
import sys


class DayTwo(Solution):
    
    def __init__(self):
        self._setup('daytwo')
        self.RED_AMOUNT = 12
        self.GREEN_AMOUNT = 13
        self.BLUE_AMOUNT = 14
        self.red = 1
        self.green = 2
        self.blue = 3

    def get_games(self):
        return self.input.split('\n')

    #returns a list with -> [game_id, red_amount, green_amount, blue_amount]
    def parse_game(self, game):
        game_id = game.split(':')[0].split(' ')[1]
        reveals = game.split(':')[1].split(';')
        colors = {
                'red': 0,
                'green': 0,
                'blue': 0
                }
        for reveal in reveals:
            parts = reveal.split(',')
            for part in parts:
                part = part.strip(' ')
                part_splitted = part.split(' ')
                amount = int(part_splitted[0])
                color = part_splitted[1]
                if amount > colors[color]:
                    colors[color] = amount
        return [int(game_id)] + list(colors.values())

    def part_one(self):
        games = self.get_games()
        valid_ids_sum = 0
        for game in games:
            if game == '':
                continue
            parsed_game = self.parse_game(game)
            valid_ids_sum += parsed_game[0] if self.is_valid_game(parsed_game) else 0
        return valid_ids_sum

    def is_valid_game(self, game) -> bool:
        return game[self.red] <= self.RED_AMOUNT and game[self.green] <= self.GREEN_AMOUNT and game[self.blue] <= self.BLUE_AMOUNT

    def part_two(self):
        games = self.get_games()
        powers_sum = 0
        for game in games:
            if game == '':
                continue
            parsed_game = self.parse_game(game)
            product = self.get_power(parsed_game)
            powers_sum += product
        return powers_sum

    def get_power(self, game):
        return game[self.red] * game[self.green] * game[self.blue]


DayTwo().run(sys.argv[1])
