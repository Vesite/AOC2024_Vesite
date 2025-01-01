# https://adventofcode.com/2024/day/1

import helpers

input_lines = helpers.get_input_as_lines("1/input.txt")

# Split the input "lines" into 2 arrays 
inputs_left = []
inputs_right = []
for line in input_lines:
    parts = line.split() # Split() Defaults to removing all whitespace, (Split(" ") Only removed one)
    inputs_left.append(int(parts[0]))
    inputs_right.append(int(parts[1]))

# Sort both list in ascending order
inputs_left.sort(reverse=False)
inputs_right.sort(reverse=False)

# Find a list of the differences
difference_list = []
for _i in range(len(inputs_left)):
    diff = abs(inputs_left[_i] - inputs_right[_i])
    difference_list.append(diff)

print("The total distance between the lists: {}".format(sum(difference_list)))

# --- Part 2 ---
similarity_score_list = []
for _i, number_check in enumerate(inputs_left):
    # Count how many times "number_check" appears in the second list
    temp_counter = inputs_right.count(number_check)
    
    similarity_score_list.append(number_check*temp_counter)

print("The Similarity score: {}".format(sum(similarity_score_list)))
