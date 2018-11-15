RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
MOVE_ROW = [0, 1, 0, -1]
MOVE_COL = [1, 0, -1, 0]


def past_limit(row, col, matrix):
    return row >= len(matrix) or col >= len(matrix) or matrix[row][col] > 0


def spiral(n, start=1):
    """
    Print the outside values in a grid and spiral towards the middle.
    For example:
    n = 4
    Returns this matrix:
     1  2  3  4
    12 13 14  5
    11 16 15  6
    10  9  8  7

    :param n: x and y size of the spiral
    :param start: start value for the matrix at top-left
    :return: matrix for the spiral
    """
    matrix = [[0 for column in range(n)] for row in range(n)]

    row = 0
    col = 0
    direction = RIGHT
    value = start

    while value < n * n + start:
        matrix[row][col] = value
        row += MOVE_ROW[direction]
        col += MOVE_COL[direction]
        if past_limit(row, col, matrix):
            new_direction = (direction + 1) % 4
            row = row - MOVE_ROW[direction] + MOVE_ROW[new_direction]
            col = col - MOVE_COL[direction] + MOVE_COL[new_direction]
            direction = new_direction
        value += 1

    return matrix


if __name__ == '__main__':
    n = 4
    result = spiral(4)
    print("spiral(%d):" % n)

    for i in range(n):
        print(result[i])
