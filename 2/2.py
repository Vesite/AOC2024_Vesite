# https://adventofcode.com/2024/day/2

def run():

    with open('2/input.txt', 'r') as file:
        # read the file line by line
        input_lines = file.readlines()
        input_lines = [line.strip() for line in input_lines]

    # Function to check if a report is safe
    def is_safe(_report):

        is_safe_increasing = True
        is_safe_decreasing = True
        
        for _i, value in enumerate(_report):
            if (_i == (len(_report) - 1)): break # Exit / Skip the final value _i

            value = int(value)
            value_next = int(_report[_i + 1])

            # Return false if the jump is too big
            if (abs(value - value_next) > 3):
                return False

            # Set "safe_increase" to false if we are decreasing or equal
            if (value >= value_next):
                is_safe_increasing = False
            # Set "safe_decrease" to false if we are increasing or equal
            if (value <= value_next):
                is_safe_decreasing = False
        
        return (is_safe_increasing or is_safe_decreasing)


    def is_safe_with_dampener(_report):
        # Here I check all variations of "_report" with _is_safe(), with one element missing
        # Ff any of the alternative "_report" are safe it will return true
        for _i in range(len(_report)):
            alternative_report = _report[:] # Copy the list
            alternative_report.pop(_i)
            if (is_safe(alternative_report)):
                return True
        
        return False

    safe_report_count_without_dampener = 0
    safe_report_count_with_dapener = 0
    for line in input_lines:
        current_report = line.split()
        if (is_safe(current_report)):
            safe_report_count_without_dampener += 1
        if (is_safe_with_dampener(current_report)):
            safe_report_count_with_dapener += 1

    print("Amount of safe reports (without dampener): {}".format(safe_report_count_without_dampener))
    print("Amount of safe reports (with dampener): {}".format(safe_report_count_with_dapener))


# Call run() if executed directly
if __name__ == "__main__":
    run()
