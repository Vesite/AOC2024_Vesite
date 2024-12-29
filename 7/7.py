
with open('7/input.txt', 'r') as file:
        # read the file line by line
        input_lines = file.readlines()
        input_lines = [line.strip() for line in input_lines]

for _i in range(len(input_lines)):
        input_lines[_i] = input_lines[_i].replace(":", "")
        input_lines[_i] = input_lines[_i].split()

# Run "int()" on all elements
input_lines = [[int(x) for x in sublist] for sublist in input_lines]

sum = 0

for line in input_lines:
    target = line.pop(0)

    result_values = [line.pop(0)]

    while (len(line) >= 1):

        # Modify the "result_values"
        # Move through all values we currently have
        # Try both "+" and "*" until the end always doubling the list's size
        result_values_copy = []
        for _i in range(len(result_values)):
            result_values_copy.append(result_values[_i]+line[0])
            result_values_copy.append(result_values[_i]*line[0])
            temp_str = str(result_values[_i]) + str(line[0])
            result_values_copy.append(int(temp_str))
        result_values = result_values_copy
        line.pop(0)

    # Check if the result in in our "result_values"
    if target in result_values:
        #print("Target: {}".format(target))
        sum += target

print(f"The total calibration result of the true equations (part 2): {sum}")

