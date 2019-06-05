RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
MOVE_ROW = [0, 1, 0, -1]
MOVE_COL = [1, 0, -1, 0]


def past_limit(row, col, matrix):
    """
    Check if row or col is outside range of the matrix.
    :param row: row number
    :param col: column number
    :param matrix: the matrix
    :return: true if row or column is out of matrix or has been visited
    """
    return row >= len(matrix) or col >= len(matrix) or matrix[row][col] > 0


def spiral(matrix_size, start_value=1):
    """
    Print the outside values in a matrix and spiral towards the middle.
    For example:
    matrix_size = 4
    Returns this matrix:
     1  2  3  4
    12 13 14  5
    11 16 15  6
    10  9  8  7

    matrix_size = 5
    start_value = 2
    Returns this matrix:
     2  3  4  5  6
    17 18 19 20  7
    16 25 26 21  8
    15 24 23 22  9
    14 13 12 11 10

    :param matrix_size: number of rows and columns in the matrix
    :param start_value: start value for the matrix at top-left
    :return: matrix for the spiral
    """
    if start_value <= 0:
        raise ValueError("start_value must be > 0 for past_limit to work")

    matrix = [[0 for column in range(matrix_size)] for row in range(matrix_size)]

    row = 0
    column = 0
    direction = RIGHT
    value = start_value

    while value < matrix_size * matrix_size + start_value:
        matrix[row][column] = value
        row += MOVE_ROW[direction]
        column += MOVE_COL[direction]
        if past_limit(row, column, matrix):
            new_direction = (direction + 1) % 4
            row = row - MOVE_ROW[direction] + MOVE_ROW[new_direction]
            column = column - MOVE_COL[direction] + MOVE_COL[new_direction]
            direction = new_direction
        value += 1

    return matrix


if __name__ == '__main__':
    n = 4
    result = spiral(4)
    print("spiral(%d):" % n)

    for i in range(n):
        print(result[i])
