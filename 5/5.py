# https://adventofcode.com/2024/day/5

def run():

    import math

    with open('5/input.txt', 'r') as file:
        # read the file line by line
        input_lines = file.readlines()
    
    # Gets the input into list variables  
    rules = []
    update_numbers = []
    first_half_of_input = True
    for line in input_lines:
        line = line.strip()
        
        if (line == ""):
            first_half_of_input = False

        if first_half_of_input:
            rules.append(line.split("|"))
        elif (line != ""):
            update_numbers.append(line.split(","))   

    # Convert all elements to integers using nested list comprehension
    rules = [[int(x) for x in sublist] for sublist in rules]
    update_numbers = [[int(x) for x in sublist] for sublist in update_numbers]
    update_numbers_incorrect = []

    # Create a map where the keys are every unique number in "rules"
    # The value is a tuple with 2 lists, one for numbers above it and one for numbers below it
    # All values are int
    rules_data_map = {}
    for rule in rules:
        number_1 = rule[0]
        number_2 = rule[1]

        # New additions to the map
        if not (number_1 in rules_data_map):
            rules_data_map[number_1] = ([], [])
        if not (number_2 in rules_data_map):
            rules_data_map[number_2] = ([], [])

        # Add "number_2" into the "below" part for number 1
        rules_data_map[number_1][1].append(number_2)
        # Add "number_1" into the "above" part for number_2
        rules_data_map[number_2][0].append(number_1)



    def check_line_is_valid(_line):

        # If it finds anything wrong in the numbers it will return "False"
        for _i in range(len(_line)):
            numbers_before = _line[:_i]
            numbers_after = _line[(_i+1):]
            tuple_from_map = rules_data_map[_line[_i]]

            # The number is valid if
            # All numbers "numbers_after" are in the tuple_from_map[1]
            result_1 = all((_x in tuple_from_map[1]) for _x in numbers_after)
            
            # All numbers "numbers_before" must be in tuple_from_map[0]
            result_2 = all((_x in tuple_from_map[0]) for _x in numbers_before)

            if not (result_1 and result_2):
                return False
        
        return True

    # This will take an update line as an arguemnt and return a fixed version
    def fix_a_update_line(_line):
        
        # The logic here basically checks what number should be placed first in the line
        # Then puts it aside and repeats on the remaining numbers
        # Until the "_line" has one element left
        new_line = []
        while (len(_line) > 1):
            front_number = find_first_in_update_line(_line)
            _line.remove(front_number)
            new_line.append(front_number)

        return new_line

    # Will return the element in the list that should be placed first
    def find_first_in_update_line(_update_line):

        for _i in range(len(_update_line)):
            numbers_before = _update_line[:_i]
            numbers_after = _update_line[(_i+1):]
            numbers_other = numbers_before + numbers_after
            tuple_from_map = rules_data_map[_update_line[_i]]

            # Check if this number "_update_line[_i]" has all the other numbers in tuple_from_map[1]
            if all((_x in tuple_from_map[1]) for _x in numbers_other):
                return _update_line[_i]
        
        # Should never reach here
        print("Error something went wrong")
        return _update_line[0]

    # Part 1 Calculation
    total_sum_part_1 = 0
    for line in update_numbers:
        # Checkinf if this line is valid
        if (check_line_is_valid(line)):
            middle_index = math.floor(len(line)/2)
            total_sum_part_1 += line[middle_index]
        else:
            update_numbers_incorrect.append(line)

    print("Total Sum Part 1: {}".format(total_sum_part_1))
            
    # Part 2
    update_numbers_fixed = []
    for line in update_numbers_incorrect:
        update_numbers_fixed.append(fix_a_update_line(line))
    
    # Part 2 Calculation
    total_sum_part_2 = 0
    for line in update_numbers_fixed:
        middle_index = math.floor(len(line)/2)
        total_sum_part_2 += line[middle_index]
    
    print("Total Sum Part 2: {}".format(total_sum_part_2))


# Call run() if executed directly
if __name__ == "__main__":
    run()

