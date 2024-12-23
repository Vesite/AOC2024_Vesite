
with open('9/input.txt', 'r') as file:
    # read the file line by line
    input_line = file.read()


blocks_part_1 = []
is_file = True
current_id = 0

# Create the "blocks_part_1" list
for char in input_line:
    
    if (is_file):
        for i in range(int(char)):
            blocks_part_1.append(str(current_id))
        current_id += 1
    if not (is_file):
        for i in range(int(char)):
            blocks_part_1.append(".")
    is_file = not is_file

blocks_copy = blocks_part_1[:]

# Compress the "blocks_part_1"
# Putting all numbers at the start
i = 0
while (i < len(blocks_part_1)):
    if blocks_part_1[i] == ".":
        # Take the number from the end at put it here
        final_value = blocks_part_1.pop()
        while final_value == ".":
            final_value = blocks_part_1.pop()

        blocks_part_1[i] = final_value
    i += 1

# Calculate sum part 1
checksum = 0
current_id = 0
for i in range(len(blocks_part_1)):
    checksum += int(blocks_part_1[i])*i
    current_id += 1

# Part 2

# This is a list of tuples
big_blocks_tuples = []
current_id = blocks_copy[0]
count = 0

# Create "big_blocks_tuples"
for value in blocks_copy:
    if value == current_id: # When its the same one
        count += 1
    else:
        big_blocks_tuples.append((current_id, count))
        current_id = value
        count = 1

# Append the last segment
if current_id != '.':
    big_blocks_tuples.append((current_id, count))

print(big_blocks_tuples)
print("")

big_blocks_tuples_copy = big_blocks_tuples[:]

length = len(big_blocks_tuples)

# Repeat this n many times
extra_space_total = 0
index_to_try_to_move_from_the_end = len(big_blocks_tuples_copy) - 1
for _n in range(len(big_blocks_tuples_copy)):

    tuple_to_try_to_move = big_blocks_tuples[index_to_try_to_move_from_the_end]
    # print("tuple_to_try_to_move: {}".format(tuple_to_try_to_move))

    for index, front_tuple in enumerate(big_blocks_tuples): # Look for a free space that fits
        if (front_tuple[0] == ".") and tuple_to_try_to_move[0] != "." and (front_tuple[1] >= tuple_to_try_to_move[1]) and (index < index_to_try_to_move_from_the_end):
            # print("Moving {} to index {}".format(tuple_to_try_to_move, index))
            extra_space = front_tuple[1] - tuple_to_try_to_move[1]
            # print("extra_space: {}".format(extra_space))

            # Replace the tuple we are moving with "."
            big_blocks_tuples[index_to_try_to_move_from_the_end] = (".", tuple_to_try_to_move[1])

            big_blocks_tuples[index] = tuple_to_try_to_move # Replace the "." space with the tuple

            # Add back whats left of the "." space
            if (extra_space > 0):
                big_blocks_tuples.insert(index + 1, (".", extra_space))
                index_to_try_to_move_from_the_end += 1

            break
    
    # print("Full list: {}".format(big_blocks_tuples))

    index_to_try_to_move_from_the_end -= 1


# Convert the tuple list back to blocks
blocks_part_2 = []
for index, tuple in enumerate(big_blocks_tuples):
    for _i in range(tuple[1]):
        blocks_part_2.append(tuple[0])

# Calculate sum part 2
checksum_2 = 0
current_id = 0
for i in range(len(blocks_part_2)):
    if blocks_part_2[i][0] != ".":
        checksum_2 += int(blocks_part_2[i])*i
        current_id += 1

print("The checksum is: {}".format(checksum))
print("The checksum part 2 is: {}".format(checksum_2))







