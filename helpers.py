

# Will take a path to a input.txt file and convert it to a list of lines
def get_input_as_lines(_input_path):
    with open(_input_path, 'r') as file:
        # read the file line by line
        input_lines = file.readlines()
        input_lines = [line.strip() for line in input_lines]
    
    return input_lines

# Will convert a list of lines into a 2D grid, list of lists
# Create a 2D Grid that i can access with indexes [_x][_y]
def string_to_grid(_list_of_lines):
    grid = []
    for _i in range(len(_list_of_lines[0])):
        column = []
        for line in _list_of_lines:
                column.append(line[_i])
        grid.append(column)
    
    return grid

