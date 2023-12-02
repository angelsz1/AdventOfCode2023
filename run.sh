#! /bin/bash

dir=$1
part=$2
numbers=(" " "one" "two" "three" "four" "five" "six" "seven" "eight" "nine" "ten" "eleven" "twelve" "thirteen" "fourteen" "fifteen" "sixteen" "seventeen" "eighteen" "nineteen" "twenty" "twenty-one" "twenty-two" "twenty-three" "twenty-four" "twenty-five")
DAY=day${numbers[$dir]}

python3 code/$DAY.py $part
