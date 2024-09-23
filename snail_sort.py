"""Snail sort from Code Wars"""

"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
"""

def go_right(grid, col_min, col_max, row_min):
    snail = []
    for i in range(col_min, col_max):
        snail.append(grid[row_min][i])
    return snail

def go_down(grid, row_min, row_max, col_max):
    snail = []
    for i in range(row_min , row_max):
        snail.append(grid[i][col_max])
    return snail

def go_left(grid, col_min, row_max):
    snail = []
    for i in reversed(range(col_min, row_max)):
        snail.append(grid[row_max][i])
    return snail

def go_up(grid, row_min , row_max, col_min):
    snail = []
    for i in reversed(range(row_min , row_max)):
        snail.append(grid[i][col_min])
    return snail


def snail(grid):

    snail = []

    row_max = len(grid)
    col_max  = row_max

    num_elements = row_max*row_max

    row_min = 0
    col_min = 0

    while(len(snail) < num_elements):
        snail.extend(go_right(grid, col_min, col_max, row_min))
        row_min += 1
        col_max -= 1
        snail.extend(go_down(grid, row_min, row_max, col_max))
        row_max -= 1
        snail.extend(go_left(grid, col_min, row_max))
        snail.extend(go_up(grid, row_min, row_max, col_min))
        col_min += 1

    return snail


def main():
    grid = [[1,  2,  3,  4,  5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]]

    print(snail(grid))


main()