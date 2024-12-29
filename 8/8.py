
with open('8/input.txt', 'r') as file:
        # read the file line by line
        input_lines = file.readlines()
        input_lines = [line.strip() for line in input_lines]

# Create a 2D Grid that i can access with indexes [_x][_y]
# Should make a simple function for this
grid = []
for _i in range(len(input_lines[0])):
        column = []
        for line in input_lines:
                column.append((line[_i], 0))
        grid.append(column)

width = len(input_lines[0]) - 1
height = len(grid[0]) - 1
#print(width)
#print(height)
# Count the amount of "#" / "frequencies" in unique locations,
# but also count them if they overlap with an antenna

# Create a map with lists of coordinates for all the signal types
# ("A" [(8, 1), (7, 3)])
antenna_map = {}
for _x in range(len(grid)):
        for _y in range(len(grid)):
                tuple = grid[_x][_y]
                char = tuple[0]
                if (char != "."):
                        if (antenna_map.get(char, "dont_exist") == "dont_exist"):
                                antenna_map[char] = [(_x, _y)] # Create a new list
                        else:
                                (antenna_map[char]).append((_x, _y)) # Add to existing list    

# Use "antenna_map" find all the spots to look to place a "#" in our grid
# And for each one "move" to each other one, then try to "move" again
# If that spot is inside the grid, add a "#" in the location

for key in antenna_map:
        position_list = antenna_map[key]
        for position_1 in position_list:
                for position_2 in position_list:
                        if (position_1 != position_2):
                                # Check if moving from position 1 to position 2 2x will put us outside the grid
                                
                                # The movement from position_1 to position_2
                                diff_x = position_2[0] - position_1[0]
                                diff_y = position_2[1] - position_1[1]

                                # Move from position 1 adding diff until we are out of bounds
                                mult = 1
                                check_x = position_1[0] + diff_x*mult
                                check_y = position_1[1] + diff_y*mult
                                is_inside_bounds = (0 <= check_x <= width) and (0 <= check_y <= height)
                                while is_inside_bounds:
                                        # Add the "#"
                                        tuple = grid[check_x][check_y] # Edit the tuple at this position
                                        new_tuple = (tuple[0], "#")
                                        grid[check_x][check_y] = new_tuple

                                        mult += 1
                                        check_x = position_1[0] + diff_x*mult
                                        check_y = position_1[1] + diff_y*mult
                                        is_inside_bounds = (0 <= check_x <= width) and (0 <= check_y <= height)


                                # check_x = position_1[0] + diff_x*2
                                # check_y = position_1[1] + diff_y*2
                                # if 
                                #         tuple = grid[check_x][check_y] # Edit the tuple at this position
                                #         new_tuple = (tuple[0], "#")
                                #         grid[check_x][check_y] = new_tuple

#print(grid)


# Count amount of "#" in the grid
count = 0
for _x in range(len(grid)):
        for _y in range(len(grid)):
                tuple = grid[_x][_y]
                if (tuple[1] == "#"):
                        count += 1


print("Total unique location with an antinode (part 2): {}".format(count))
