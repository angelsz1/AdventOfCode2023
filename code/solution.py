from reader import Reader


class Solution:
    
    def _setup(self, name):
        self.name = name
        self.inputp1 = self.get_input("inputp1.in")
        self.inputp2 = self.get_input("inputp2.in")
        self.examplep1 = self.get_input("examplep1.in")
        self.examplep2 = self.get_input("examplep2.in")
        self.input = self.examplep1

    def part_one(self):
        pass

    def part_two(self):
        pass

    def run(self, part):
        if part == str(1):
            print("--------- Example ----------\n")
            print(self.part_one())
            self.input = self.inputp1
            print("--------- Real input ----------\n")
            print(self.part_one())
        else:
            self.input = self.examplep2
            print("--------- Example ----------\n")
            print(self.part_two())
            self.input = self.inputp2
            print("--------- Real input ----------\n")
            print(self.part_two())

    def get_input(self, filename):
        reader = Reader(self.name, filename)
        return reader.read()

