# https://adventofcode.com/2024/day/3

import re

with open('3/input.txt', 'r') as file:
    # read the file line by line
    input_line = file.read()

total_sum_part_1 = 0

# This is the pattern for the Regular Expressions (Regex)
# Finds all mul() functions in the input string
pattern = r"mul\(\d+\,\d+\)"
matches = re.findall(pattern, input_line)

# Multiply all the numbers together
for string in matches:
    numbers = re.findall(r"\d+", string) # This pattern will find any numbers with 1 or more characters
    total_sum_part_1 += int(numbers[0]) * int(numbers[1])

print("The total sum in part 1: {}".format(total_sum_part_1))

# Part 2
total_sum_part_2 = 0

# Regex Pattern looking for the 3 different things using OR operator (|)
pattern = r"mul\(\d+\,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, input_line)

# Multiply the numbers, only if there is a "do()"" before it
ok_to_mul = True
for string in matches:
    
    if ((string[0:3] == "mul") and (ok_to_mul)):
        numbers = re.findall(r"\d+", string) # This pattern will find any numbers with 1 or more characters
        total_sum_part_2 += int(numbers[0]) * int(numbers[1])

    if (string[0:3] == "do("):
        ok_to_mul = True
    if (string[0:3] == "don"):
        ok_to_mul = False

print("The total sum in part 2: {}".format(total_sum_part_2))
