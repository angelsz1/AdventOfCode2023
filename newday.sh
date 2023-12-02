#! /bin/bash
numbers=(" " "one" "two" "three" "four" "five" "six" "seven" "eight" "nine" "ten" "eleven" "twelve" "thirteen" "fourteen" "fifteen" "sixteen" "seventeen" "eighteen" "nineteen" "twenty" "twenty-one" "twenty-two" "twenty-three" "twenty-four" "twenty-five")
dir=$1
DAY=day${numbers[$dir]}

mkdir input/$DAY
touch code/$DAY.py
touch input/$DAY/inputp1.in
touch input/$DAY/inputp2.in
touch input/$DAY/examplep1.in
touch input/$DAY/examplep2.in
