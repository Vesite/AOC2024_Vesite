
def run():
        
    import copy
    import math
    import hashlib

    with open('6/input.txt', 'r') as file:
            # read the file line by line
            input_lines = file.readlines()
            input_lines = [line.strip() for line in input_lines]

    # Convert into 2D List of List, where each element is a character
    input_2D_list = []
    for line in input_lines:
        input_2D_list.append(list(line))

    # Set to store the positions the guard has passed
    guard_visits = set()

    # Find the position (_x, _y) of "^",
    for _y in range(len(input_2D_list)):
        for _x in range(len(input_2D_list[0])):
            if (input_2D_list[_y][_x] == "^"):
                guard_starting_position = (_x, _y)
                guard_visits.add(guard_starting_position)

    width = len(input_2D_list[0])
    height = len(input_2D_list)

    DIRECTIONS = {
        "up":       {"offset": (0, -1),     "next_direction": "right"},
        "right":    {"offset": (1, 0),      "next_direction": "down"},
        "down":     {"offset": (0, 1),      "next_direction": "left"},
        "left":     {"offset": (-1, 0),     "next_direction": "up"}
    }

    current_direction = "up"
    guard_position = guard_starting_position
    # First Variable Update
    dx, dy = DIRECTIONS[current_direction]["offset"]
    check_x = int(guard_position[0] + dx)
    check_y = int(guard_position[1] + dy)
    is_out_of_bounds = (check_x < 0 or check_x >= width or check_y < 0 or check_y >= height)

    while not (is_out_of_bounds):
        
        if (input_2D_list[check_y][check_x] == "#"):
            # If "#" then only turn
            current_direction = DIRECTIONS[current_direction]["next_direction"]
        elif (input_2D_list[check_y][check_x] == "." or input_2D_list[check_y][check_x] == "^"):
            # If "." Then save that position and move "guard_position"
            guard_position = (check_x, check_y)
            guard_visits.add(guard_position)
        
        # Repeating Variable Update
        dx, dy = DIRECTIONS[current_direction]["offset"]
        check_x = int(guard_position[0] + dx)
        check_y = int(guard_position[1] + dy)
        is_out_of_bounds = (check_x < 0 or check_x >= width or check_y < 0 or check_y >= height)

    print("Distinct Positions (part 1): {}".format(len(guard_visits)))

    # Part 2 --------------------------------------------------------------------------------

    # Will look for a repeating pattern in the full history of the guard
    # If it finds one that is repeated exactly 2 times then that means he is stuck in a loop
    # The function "is_list_repeating" checks this

    # Instead of cheking "is_list_repeating" we could also store the direction in the "guard_full_path"
    # Then we can just look for if we have been in that exact position before and we know we are stuck in a loop
    def check_if_stuck(_2D_grid):
        
        guard_path_set = set()
        current_direction = "up"
        guard_state = (guard_starting_position[0], guard_starting_position[1], current_direction)
        guard_path_set.add(guard_state)

        # First Variable Update
        dx, dy = DIRECTIONS[current_direction]["offset"]
        check_x = int(guard_state[0] + dx)
        check_y = int(guard_state[1] + dy)
        is_out_of_bounds = (check_x < 0 or check_x >= width or check_y < 0 or check_y >= height)

        while not (is_out_of_bounds):

            if (_2D_grid[check_y][check_x] == "#"):
                # If "#" then only turn
                current_direction = DIRECTIONS[current_direction]["next_direction"]
            elif ((_2D_grid[check_y][check_x] == ".") or (_2D_grid[check_y][check_x] == "^")):
                # If "." Then save that position and move "guard_state"
                guard_state = (check_x, check_y, current_direction)
                if (guard_state in guard_path_set):
                    return True # We have been in this state before
                else:
                    guard_path_set.add(guard_state)
                    
            # Repeating Variable Update
            dx, dy = DIRECTIONS[current_direction]["offset"]
            check_x = int(guard_state[0] + dx)
            check_y = int(guard_state[1] + dy)
            is_out_of_bounds = (check_x < 0 or check_x >= width or check_y < 0 or check_y >= height)

        return False
    
    # Count how many times the guard is stuck, on every variation of the grid
    stuck_grids_count = 0
    for _y in range(len(input_2D_list)):
        for _x in range(len(input_2D_list[0])):
            if (input_2D_list[_y][_x] == "."):
                input_2D_list[_y][_x] = "#" # Temporary change it to "#""

                # Debug
                print("Checking: {}".format((_x, _y)))
                #print("Counter: {}".format(stuck_grids_count))

                if (check_if_stuck(input_2D_list)):
                    stuck_grids_count += 1
                
                # Change the grid back to normal
                input_2D_list[_y][_x] = "."

    print("Amount of possible ways we can get the guard stuck: {}".format(stuck_grids_count))

# Call run() if executed directly
if __name__ == "__main__":
    run()
