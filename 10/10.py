
def run():

    import helpers 

    input_lines = helpers.get_input_as_lines("10/input.txt")
    grid = helpers.string_to_grid(input_lines)
    
    width = len(input_lines[0])
    height = len(grid[0])

    def count_trailhead_1(_x, _y, _n, _current_score, _grid):

        width = len(_grid)
        height = len(_grid[0])

        if (_n == 9) and (not (_x, _y) in visited):
            return 1
        
        new_n = _n + 1
        
        # Check the left
        if (0 <= (_x + 1) <= (width - 1)) and (int(_grid[_x + 1][_y]) == new_n):
            #print("Checking left n={}".format(new_n))
            value = count_trailhead_1(_x + 1, _y, new_n, 0, _grid)
            _current_score += value
            if (value == 1):
                visited.append((_x + 1, _y))
        
        # Check the right
        if (0 <= (_x - 1) <= (width - 1)) and (int(_grid[_x - 1][_y]) == new_n):
            #print("Checking right n={}".format(new_n))
            value = count_trailhead_1(_x - 1, _y, new_n, 0, _grid)
            _current_score += value
            if (value == 1):
                visited.append((_x - 1, _y))
        
        # Check down
        if (0 <= (_y + 1) <= (height - 1)) and (int(_grid[_x][_y + 1]) == new_n):
            value = count_trailhead_1(_x, _y + 1, new_n, 0, _grid)
            _current_score += value
            if (value == 1):
                visited.append((_x, _y + 1))

        # Check up
        if (0 <= (_y - 1) <= (height - 1)) and (int(_grid[_x][_y - 1]) == new_n):
            value = count_trailhead_1(_x, _y - 1, new_n, 0, _grid)
            _current_score += value
            if (value == 1):
                visited.append((_x, _y - 1))
        
        return _current_score

    def count_trailhead_2(_x, _y, _n, _current_score, _grid):

        width = len(_grid)
        height = len(_grid[0])

        if (_n == 9):
            return 1
        
        new_n = _n + 1
        
        # Check the left
        if (0 <= (_x + 1) <= (width - 1)) and (int(_grid[_x + 1][_y]) == new_n):
            #print("Checking left n={}".format(new_n))
            value = count_trailhead_2(_x + 1, _y, new_n, 0, _grid)
            _current_score += value
        
        # Check the right
        if (0 <= (_x - 1) <= (width - 1)) and (int(_grid[_x - 1][_y]) == new_n):
            #print("Checking right n={}".format(new_n))
            value = count_trailhead_2(_x - 1, _y, new_n, 0, _grid)
            _current_score += value
        
        # Check down
        if (0 <= (_y + 1) <= (height - 1)) and (int(_grid[_x][_y + 1]) == new_n):
            value = count_trailhead_2(_x, _y + 1, new_n, 0, _grid)
            _current_score += value

        # Check up
        if (0 <= (_y - 1) <= (height - 1)) and (int(_grid[_x][_y - 1]) == new_n):
            value = count_trailhead_2(_x, _y - 1, new_n, 0, _grid)
            _current_score += value
        
        return _current_score


    trailheads_part_1 = 0
    trailheads_part_2 = 0
    for _x in range(width):
        for _y in range(height):
            if (int(grid[_x][_y]) == 0):
                visited = []
                value = count_trailhead_1(_x, _y, 0, 0, grid)
                #print("found {} on {}, {}".format(value, _x, _y))
                trailheads_part_1 += value

                value = count_trailhead_2(_x, _y, 0, 0, grid)
                trailheads_part_2 += value


    print("Amounts of trail heads part 1: {}".format(trailheads_part_1))
    print("Amounts of trail heads part 2: {}".format(trailheads_part_2))


# Call run() if executed directly
if __name__ == "__main__":
    run()

