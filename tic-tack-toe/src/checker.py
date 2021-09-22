def check_horizontally(matrix):
    for row in range(len(matrix)):
        if matrix[row].count("X") == 3 or matrix[row].count("O") == 3:
            return True
        continue
    return False


def check_vertically(matrix):
    if [matrix[0][0], matrix[1][0], matrix[2][0]].count("X") == 3 or [matrix[0][0], matrix[1][0], matrix[2][0]].count(
            "O") == 3:
        return True
    if [matrix[0][1], matrix[1][1], matrix[2][1]].count("X") == 3 or [matrix[0][1], matrix[1][1], matrix[2][1]].count(
            "O") == 3:
        return True
    if [matrix[0][2], matrix[1][2], matrix[2][2]].count("X") == 3 or [matrix[0][2], matrix[1][2], matrix[2][2]].count(
            "O") == 3:
        return True
    return False


def check_diagonally(matrix):
    if [matrix[0][0], matrix[1][1], matrix[2][2]].count("X") == 3 or [matrix[0][0], matrix[1][1], matrix[2][2]].count(
            "O") == 3:
        return True
    if [matrix[2][0], matrix[1][1], matrix[0][2]].count("X") == 3 or [matrix[2][0], matrix[1][1], matrix[0][2]].count(
            "O") == 3:
        return True
    return False
