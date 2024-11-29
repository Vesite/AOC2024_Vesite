# Run this file and enter input to run any of the other file, it will also print and save the runtime of the program

import time
from pathlib import Path

def main():
    while True:

        user_input = input("Enter the day you want to run (a number from 1 to 24):")

        # Print "Invalid input" if the input is wrong, break out if the input is correct
        try:
            user_number = int(user_input)
            if (1 <= int(user_input) <= 25):
                # Check if the day exits
                file_path = Path(user_input) / f"{user_input}.py"
                if file_path.is_file():
                    break # Will continue to the execution of the file
                else:
                    print("This day's files does not exist yet")
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    print("Running File: {}".format(file_path))

    # Measure the time before running the day's script
    start_time = time.perf_counter()

    # Open and run the file
    with open(file_path) as f:
        script_contents = f.read()
    exec(script_contents)

    # Measure the time after running the day's script
    end_time = time.perf_counter()
    # Calculate the difference to find out how long the operation took
    elapsed_time = end_time - start_time
    # Print the elapsed time
    seconds_string = round(elapsed_time, 3)
    miliseconds_string = round(elapsed_time*1000, 3)
    microseconds_string = round(elapsed_time*1000*1000, 3)
    result_string = "Day {} took {} seconds ({} Milliseconds) ({} Microseconds)".format(user_input, seconds_string, miliseconds_string, microseconds_string)
    print(result_string)

    # Make a new file in the folder and store the results
    file_name = user_input + "/time_result.txt"
    with open(file_name, "w") as file_path:
        file_path.write(result_string)


if __name__ == "__main__":
    main()