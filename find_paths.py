from pprint import pprint
from random import randrange


def main():
    memo = {}
    grid = [[' ' for i in range(10)] for j in range(10)]
    for _ in range(30):
        rand_row = randrange(len(grid))
        rand_col = randrange(len(grid[0]))
        grid[rand_row][rand_col] = 'X'

    pprint(grid)
    print(find_num_paths(grid, 0, 0, memo))
    pprint(grid)


def find_num_paths(grid, row, col, memo):
    if row == 9 and col == 9:
        return 1

    if row > 9 or col > 9:
        return 0

    if grid[row][col] == 'X':
        return 0

    if (row, col) in memo.keys():
        return memo[(row, col)]

    grid[row][col] = '0'
    return find_num_paths(grid, row + 1, col, memo) + find_num_paths(grid, row, col + 1, memo)


if __name__ == '__main__':
    main()
