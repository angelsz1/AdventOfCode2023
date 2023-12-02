from solution import Solution
import sys
import re


class DayOne(Solution):

    def __init__(self):
        self._setup('dayone')

    def part_one(self):
        listOfNumbers = self.getOnlyNumsAsList()
        return self.sumArrLastAndFirstNum(listOfNumbers)

    def sumArrLastAndFirstNum(self, listOfNumbers):
        totalSum = 0
        for number in listOfNumbers:
            firstNumber = number[0]
            lastNumber = number[len(number) - 1]
            finalNumber = firstNumber + lastNumber
            totalSum += int(finalNumber)
        return totalSum


    def part_two(self):
        listOfNumbers = self.getNumsAndSpelledNumsAsList()
        print(listOfNumbers)
        return self.sumArrLastAndFirstNum(listOfNumbers)

    def getNumsAndSpelledNumsAsList(self):
        number_mapping = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0'
        }
        for word, number in number_mapping.items():
            self.input = self.input.replace(word, number)
        return self.getOnlyNumsAsList()

    def getOnlyNumsAsList(self):
        retList = []
        splittedInput = self.input.split('\n')
        for line in splittedInput:
            number = re.sub(r'[a-zA-Z]', '', line)
            if number != '':
                retList.append(number)
        return retList

DayOne().run(sys.argv[1])

