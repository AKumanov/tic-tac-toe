from .checker import check_horizontally, check_vertically, check_diagonally


def create_board():
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append("" * 3)
    return matrix


def check_winner(board):
    # check horizontally
    if check_horizontally(board):
        return True
    # check vertically
    if check_vertically(board):
        return True
    # check diagonally
    if check_diagonally(board):
        return True
    return False


def make_move(move, board, signs, turn):
    row, col = mapper[move]
    board[int(row)][int(col)] = signs[turn % 2]

    return board


def is_empty(move, board):
    row, col = mapper[move]
    if board[int(row)][int(col)] == "":
        return True
    return False


def is_in_range(move):
    if 1 <= move <= 9:
        return True
    return False


mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}
