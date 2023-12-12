#  File: Work.py
#  Name: Samanvitha Nukala

import sys
import time

# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep. Must be implemented
#          using recursion.
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep

def sum_series(lines_before_coffee, prod_loss):
    pass
    if lines_before_coffee == 0:
        return lines_before_coffee
    else:
        return lines_before_coffee + sum_series(lines_before_coffee // prod_loss, prod_loss)

# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee

def linear_search(total_lines, prod_loss):

    count = 0
    for lines in range(0, total_lines+1):
        count += 1
        if sum_series(lines, prod_loss) >= total_lines:
            return lines, count

# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee

def binary_search(total_lines, prod_loss):

    low = 0
    high = total_lines
    count = 0

    while high > low:
        count += 1
        mid = (high+low)//2
        completed_lines = sum_series(mid, prod_loss)
        if completed_lines < total_lines:
            low = mid + 1
        elif completed_lines >= total_lines:
            high = mid

    return low, count


def main():

    # Open input source
    # Change debug to false before submitting
    debug = False
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
