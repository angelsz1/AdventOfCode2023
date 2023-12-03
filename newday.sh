#! /bin/bash
numbers=(" " "one" "two" "three" "four" "five" "six" "seven" "eight" "nine" "ten" "eleven" "twelve" "thirteen" "fourteen" "fifteen" "sixteen" "seventeen" "eighteen" "nineteen" "twenty" "twenty-one" "twenty-two" "twenty-three" "twenty-four" "twenty-five")
Numbers=(" " "One" "Two" "Three" "Four" "Five" "Six" "Seven" "Eight" "Nine" "Ten" "Eleven" "Twelve" "Thirteen" "Fourteen" "Fifteen" "Sixteen" "Seventeen" "Eighteen" "Nineteen" "Twenty" "Twenty-One" "Twenty-Two" "Twenty-Three" "Twenty-Four" "Twenty-Five")
dir=$1
DAY=day${numbers[$dir]}

mkdir input/$DAY
touch code/$DAY.py
touch input/$DAY/inputp1.in
touch input/$DAY/inputp2.in
touch input/$DAY/examplep1.in
touch input/$DAY/examplep2.in
cat <<EOF >> code/$DAY.py
import sys
from solution import Solution


class Day${Numbers[$dir]}(Solution):

    def __init__(self):
        self._setup('$DAY')

    def part_one(self):
        pass

    def part_two(self):
        pass

Day${Numbers[$dir]}().run(sys.argv[1])
EOF
