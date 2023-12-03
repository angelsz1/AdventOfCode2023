from solution import Solution
import sys
import re


class DayOne(Solution):

    def __init__(self):
        self._setup('dayone')
        self.number_mapping = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

    def part_one(self):
        listOfNumbers = self.getOnlyNumsAsList()
        return self.sumArrLastAndFirstNum(listOfNumbers)

    def sumArrLastAndFirstNum(self, listOfNumbers):
        totalSum = 0
        print(listOfNumbers)
        for number in listOfNumbers:
            firstNumber = number[0]
            lastNumber = number[len(number) - 1]
            finalNumber = firstNumber + lastNumber
            totalSum += int(finalNumber)
        return totalSum


    def part_two(self):
        listOfNumbers = self.getNumsAndSpelledNumsAsList()
        return self.sumArrLastAndFirstNum(listOfNumbers)

    def getNumsAndSpelledNumsAsList(self):
        retList = []
        splitted_input = self.input.split('\n')
        for line in splitted_input:
            number = re.sub(r'[a-zA-Z]', '', line)
            first_str, last_str = self.get_str_borders(line)
            first_num, last_num = self.get_nums_from_borders(first_str, last_str)
            number = first_num + number + last_num
            if number != '':
                retList.append(number)
        return retList
            
    def get_nums_from_borders(self, first_str, last_str):
        first_nums = {}
        last_nums = {}
        for word, _ in self.number_mapping.items():
            if first_str != '' and word in first_str:
                index = first_str.index(word)
                first_nums[index] = word
            if last_str != '' and word in last_str:
                index = last_str.index(word)
                last_nums[index] = word
        if first_nums != {}:
            first_nums = self.sanitize_fnums(first_nums)
        else:
            first_nums = ''
        if last_nums != {}:
            last_nums = self.sanitize_lnums(last_nums)
        else:
            last_nums = ''

        return first_nums, last_nums

    def sanitize_lnums(self, nums):
        sanitized = self.sanitize_nums(nums)
        return list(sanitized.values())[len(sanitized) - 1]

    def sanitize_fnums(self, nums):
        sanitized = self.sanitize_nums(nums)
        return list(sanitized.values())[0]

    def sanitize_nums(self, nums):
        sorted_keys = list(nums.keys())
        sorted_keys.sort()
        last_key = sorted_keys[0]
        last_num = nums[last_key]
        valid_nums = {}
        valid_nums[last_key] = self.number_mapping[last_num]
        for key in sorted_keys:
            if key == last_key:
                continue
            if key - last_key >= len(last_num):
                valid_nums[key] = self.number_mapping[nums[key]]
            last_num = nums[key]
            last_key = key
        return valid_nums

    def get_str_borders(self, line):
        splitted_line = re.split(r'[0-9]', line)
        return splitted_line[0], splitted_line[len(splitted_line) - 1]

    def getOnlyNumsAsList(self):
        retList = []
        splittedInput = self.input.split('\n')
        for line in splittedInput:
            number = re.sub(r'[a-zA-Z]', '', line)
            if number != '':
                retList.append(number)
        return retList

DayOne().run(sys.argv[1])

