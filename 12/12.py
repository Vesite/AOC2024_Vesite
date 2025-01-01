
def run():

    import helpers

    input_lines = helpers.get_input_as_lines("12/input.txt")
    grid = helpers.string_to_grid(input_lines)

    width = len(input_lines[0])
    height = len(grid[0])

    #all_data_map = {}
    region_data_list = []
    all_visited_positions = []

    # Initialize global variables only once
    global temp_positions
    global temp_perimiter_score
    temp_positions = []
    temp_perimiter_score = 0

    # Will return a list of connected letters
    def find_connected(_char, _x, _y):
        global temp_positions
        global temp_perimiter_score

        
        # Add current position
        temp_positions.append((_x, _y))

        #print(temp_positions)

        # Check Left
        check_x = (_x - 1)
        check_y = _y
        if 0 <= check_x < width:
            if grid[check_x][check_y] != _char:
                temp_perimiter_score += 1
            else:
                if not ((check_x, check_y) in temp_positions):
                    find_connected(_char, check_x, check_y)
        else:
            temp_perimiter_score += 1

        # Check Right
        check_x = (_x + 1)
        check_y = _y
        if 0 <= check_x < width:
            if grid[check_x][check_y] != _char:
                temp_perimiter_score += 1
            else:
                if not ((check_x, check_y) in temp_positions):
                    find_connected(_char, check_x, check_y)
        else:
            temp_perimiter_score += 1

        # Check Up
        check_x = _x
        check_y = (_y - 1)
        if 0 <= check_y < height:
            if grid[_x][check_y] != _char:
                temp_perimiter_score += 1
            else:
                if not ((check_x, check_y) in temp_positions):
                    find_connected(_char, check_x, check_y)
        else:
            temp_perimiter_score += 1

        # Check Down
        check_x = _x
        check_y = (_y + 1)
        if 0 <= check_y < height:
            if grid[_x][check_y] != _char:
                temp_perimiter_score += 1
            else:
                if not ((check_x, check_y) in temp_positions):
                    find_connected(_char, check_x, check_y)
        else:
            temp_perimiter_score += 1


    for _x in range(width):
        for _y in range(height):
            character = grid[_x][_y]

            if (_x, _y) not in all_visited_positions:
                # Reset temp variables only, but not the globals
                temp_positions.clear()
                temp_perimiter_score = 0
                
                find_connected(character, _x, _y)
                
                #print(f"positions: {temp_positions}")
                #print(f"perimeter score: {temp_perimiter_score}")

                data_tuple = (len(temp_positions), temp_perimiter_score, temp_positions[:])
                region_data_list.append(data_tuple)
                all_visited_positions.extend(temp_positions)

    #print(region_data_list)

    total_cost_part_1 = 0

    for tuple in region_data_list:
        total_cost_part_1 += tuple[0]*tuple[1]

    print(f"Total Cost (part 1): {total_cost_part_1}")

# Run if the script is executed directly
if __name__ == "__main__":
    run()
