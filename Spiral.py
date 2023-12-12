#  File: Spiral.py
#  Name: Samanvitha Nukala

import sys

def get_dimension(in_data):

    # reading input file

    input_file = in_data.readline()
    input_line = input_file.strip('\n')

    # checking for any non int inputs:

    try:
        n = int(input_line)
    except:
        print('Invalid data')
        n = int(in_data.readline().strip())

    # making sure the input int is odd and positive for the spiral:

    if n % 2 == 0:
        n = n + 1

    if n <= 1 or n >= 100:
        print('Invalid data')

    return n


def create_spiral(n):

    # creating 2D spiral array with 1 in the center:

    spiral = [[0] * n for value in range(n)]
    r = n // 2
    c = n // 2
    movements = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = 0
    spiral[r][c] = 1
    num = 2
    count = 1
    while num <= n ** 2:
        for i in range(count):
            r = r + directions[x][0]
            c = c + directions[x][1]
            if 0 <= r < n and 0 <= c < n:
                spiral[r][c] = num
                num += 1
        x = (x + 1) % 4
        movements += 1
        if movements % 2 == 0:
            count += 1

    return spiral


def print_adjacent_sums(in_data, spiral):

    # providing the input 'n' for the method sum_adjacent_numbers:

    # checking for any non int inputs

    for line in in_data:
        value = line.strip()
        try:
            n = int(value)
        except:
            print('Invalid data')
            n = int(in_data.readline().strip())

        sum_adjacent_numbers(spiral, n)

def sum_adjacent_numbers(spiral, n):

    # providing the sum of numbers adjacent to 'n' in a 3X3 grid excluding 'n':

    # if 'n' is not within the spiral a sum of 0 will be printed out with no error message:

    current_sum = 0
    if n > (len(spiral) * len(spiral[0])):
        print(current_sum)
    else:
        for row, col in enumerate(spiral):
            if n in col:
                r = row
                c = col.index(n)
        steps_up = (-1, 0, 1)
        steps_side = (-1, 0, 1)
        for x in steps_up:
            for y in steps_side:
                current_row = r + x
                current_col = c + y
                if 0 <= current_row < len(spiral) and 0 <= current_col < len(spiral[0]):
                    if spiral[current_row][current_col] is not None:
                        if spiral[current_row][current_col] != n:
                            current_sum += spiral[current_row][current_col]
    print(current_sum)

def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


def main():
    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
