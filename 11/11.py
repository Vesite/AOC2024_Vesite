
def run():

    import functools

    with open('11/input.txt', 'r') as file:
            # read the file line by line
            stones_string = file.readline()
            stones = stones_string.split()

    for _i, _string in enumerate(stones):
        stones[_i] = int(stones[_i])

    blinks_part_1 = 25
    blinks_part_2 = 75

    # "functools.cache" Will cache the results of the recursive function given the arugments,
    # It then only needs to calculate each possible argument once
    # Required to calculate all 75 blinks in a reasonable time
    @functools.cache
    def count_rocks(_starting_rock, _blinks):
        total = 0

        if (_blinks == 0):
            return 1

        if (_starting_rock == 0):
            _starting_rock = 1
            total += count_rocks(_starting_rock, _blinks - 1)
        else:
            length = len(str(_starting_rock))
            if (length % 2 == 0): # Check if its even
                number_string = str(_starting_rock)
                half = round(length*0.5)
                new_stone_1 = int(number_string[:half])
                new_stone_2 = int(number_string[half:])
                total += count_rocks(new_stone_1, _blinks - 1)
                total += count_rocks(new_stone_2, _blinks - 1)
            else:
                total += count_rocks(_starting_rock*2024, _blinks - 1)

        return total

    total_stones_part_1 = 0
    for stone in stones:
        total_stones_part_1 += count_rocks(stone, blinks_part_1)

    total_stones_part_2 = 0
    for stone in stones:
        total_stones_part_2 += count_rocks(stone, blinks_part_2)

    print(f"Total amount of stones after {blinks_part_1} blinks: {total_stones_part_1}")
    print(f"Total amount of stones after {blinks_part_2} blinks: {total_stones_part_2}")

# Call run() if executed directly
if __name__ == "__main__":
    run()

