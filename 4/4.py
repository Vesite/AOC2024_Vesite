# https://adventofcode.com/2024/day/4

# Could for sure compress and/or simplify the code a bit here

def run():

    with open('4/input.txt', 'r') as file:
        # read the file line by line
        input_lines = file.readlines()
        input_lines = [line.strip() for line in input_lines]

    # Convert into 2D List of List, where each element is a character
    input_2D_list = []
    for line in input_lines:
        input_2D_list.append(list(line))

    # Helper Function
    # This check will also make sure it is not out of bounds
    def check(_grid, _x, _y, _char):

        width = len(_grid[0])
        height = len(_grid)
        if (0 <= _x <= (width - 1)) and (0 <= _y <= (height - 1)):
            if (_grid[_y][_x] == _char):
                return True
        
        return False

    # Will find how many "xmas" words are on this position in the grid
    # Started on this character
    def find_amount_xmas(_grid, _x, _y):
        _amount = 0
        if (_grid[_y][_x] == "X"):

            # Right
            if check(_grid, _x + 1, _y, "M") and check(_grid, _x + 2, _y, "A") and check(_grid, _x + 3, _y, "S"):
                _amount += 1
            # Left
            if check(_grid, _x - 1, _y, "M") and check(_grid, _x - 2, _y, "A") and check(_grid, _x - 3, _y, "S"):
                _amount += 1
            # Up
            if check(_grid, _x, _y - 1, "M") and check(_grid, _x, _y - 2, "A") and check(_grid, _x, _y - 3, "S"):
                _amount += 1
            # Down
            if check(_grid, _x, _y + 1, "M") and check(_grid, _x, _y + 2, "A") and check(_grid, _x, _y + 3, "S"):
                _amount += 1
            
            # Other 4 diagonal directions
            if check(_grid, _x + 1, _y + 1, "M") and check(_grid, _x + 2, _y + 2, "A") and check(_grid, _x + 3, _y + 3, "S"):
                _amount += 1
            if check(_grid, _x - 1, _y - 1, "M") and check(_grid, _x - 2, _y - 2, "A") and check(_grid, _x - 3, _y - 3, "S"):
                _amount += 1
            if check(_grid, _x + 1, _y - 1, "M") and check(_grid, _x + 2, _y - 2, "A") and check(_grid, _x + 3, _y - 3, "S"):
                _amount += 1
            if check(_grid, _x - 1, _y + 1, "M") and check(_grid, _x - 2, _y + 2, "A") and check(_grid, _x - 3, _y + 3, "S"):
                _amount += 1
        
        # Debug
        # print("Checking {}, {}. Found {}".format(_x, _y, _amount))

        return _amount
    
    def find_amount_mas_cross(_grid, _x, _y):
        if (_grid[_y][_x] == "A"):
            
            m_count = 0
            s_count = 0
            
            # If 2 M at the top and 2 S at the bottom
            if ((check(_grid, _x - 1, _y - 1, "M") and check(_grid, _x + 1, _y - 1, "M"))
            and (check(_grid, _x - 1, _y + 1, "S") and check(_grid, _x + 1, _y + 1, "S"))):
                return 1

            # If 2 S at the top and 2 M at the bottom
            if ((check(_grid, _x - 1, _y - 1, "S") and check(_grid, _x + 1, _y - 1, "S"))
            and (check(_grid, _x - 1, _y + 1, "M") and check(_grid, _x + 1, _y + 1, "M"))):
                return 1
            
            # If 2 M at the left and 2 S at the right
            if ((check(_grid, _x - 1, _y - 1, "M") and check(_grid, _x - 1, _y + 1, "M"))
            and (check(_grid, _x + 1, _y - 1, "S") and check(_grid, _x + 1, _y + 1, "S"))):
                return 1

            # If 2 S at the left and 2 M at the right
            if ((check(_grid, _x - 1, _y - 1, "S") and check(_grid, _x - 1, _y + 1, "S"))
            and (check(_grid, _x + 1, _y - 1, "M") and check(_grid, _x + 1, _y + 1, "M"))):
                return 1

        return 0

    
        
    total_xmas = 0

    # Loop throught the 2D List, where the top left position is (0, 0).
    # Positive X direction is right. Positive Y direction is down
    for _y in range(len(input_2D_list)):
        for _x in range(len(input_2D_list[0])):
            total_xmas += find_amount_xmas(input_2D_list, _x, _y)
    
    
    print("Total Amount of \"XMAS\": {}".format(total_xmas))

    # Part 2

    total_mas_cross = 0
    for _y in range(len(input_2D_list)):
        for _x in range(len(input_2D_list[0])):
            total_mas_cross += find_amount_mas_cross(input_2D_list, _x, _y)

    print("Total Amount of \"MAS CROSS\": {}".format(total_mas_cross))


# Call run() if executed directly
if __name__ == "__main__":
    run()

