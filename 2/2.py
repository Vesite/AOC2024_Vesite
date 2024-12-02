# https://adventofcode.com/2024/day/2

with open('2/input.txt', 'r') as file:
    # read the file line by line
    input_lines = file.readlines()
    input_lines = [line.strip() for line in input_lines]

# Function to check if a report is safe
def is_safe(_report):

    is_safe_increasing = True
    is_safe_decreasing = True

    # Loop through all numbers in the report and check if thay are increasing but not too much
    for _i in range(len(_report)):
        if (_i != (len(_report) - 1)): # Not at the final _i
            
            # 2 Values to compare
            value = int(_report[_i])
            value_next = int(_report[_i + 1])

            if not ((value < value_next) and (abs(value - value_next) <= 3)): # Check if we are increasing and not too much
                is_safe_increasing = False
            if not ((value > value_next) and (abs(value - value_next) <= 3)): # Check if we are decreasing and not too much
                is_safe_decreasing = False      

    return (is_safe_increasing or is_safe_decreasing)

# I run "is_safe()" from here"
def is_safe_with_dampener(_report):
    # Here i would want to check the "_report" with _is_safe()
    # With all combinations of one element missing
    # Will loop through the list and if any of the alternative lists are safe it will return true
    for _i in range(len(_report)):
        alternative_report = _report[:] # Copy the list
        alternative_report.pop(_i)
        if (is_safe(alternative_report)):
            return True
    
    return False

safe_report_count = 0
for line in input_lines:
    current_report = line.split()
    if (is_safe_with_dampener(current_report)):
        safe_report_count += 1

print("Amount of safe reports: {}".format(safe_report_count))

