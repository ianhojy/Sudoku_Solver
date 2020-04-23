from datetime import datetime

def print_grid(arr):
    for row in range(9):
            print(' '.join([str(num) for num in arr[row]]))
        # print('\n')


def row_check(arr, row, num):
    for other in arr[row]:
        if num == other:
            return False
    return True


def col_check(arr, col, num):
    for row in arr:
        if num == row[col]:
            return False
    return True


def box_check(arr, row, col, num):
    row_left_corner = 3 * (row//3)
    col_left_corner = 3 * (col//3)
    for i in range(row_left_corner, row_left_corner + 3):
        for j in range(col_left_corner, col_left_corner + 3):
            if arr[i][j] == num:
                return False
    return True


def all_checks(arr, row, col, num):
    return row_check(arr, row, num) and col_check(arr, col, num) and box_check(arr, row, col, num)


def find_empty_cell(arr, coor):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                coor[0] = row
                coor[1] = col
                return True

    return False


def solve_grid(arr):

    start_corr = [0, 0]

    if not find_empty_cell(arr, start_corr):
        return True

    row = start_corr[0]
    col = start_corr[1]

    for num in range(1, 10):

        if all_checks(arr, row, col, num):

            arr[row][col] = num

            if solve_grid(arr):
                return True

            arr[row][col] = 0

    return False
