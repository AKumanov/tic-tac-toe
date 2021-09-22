from src.logic import main_logic


def show_board():
    print("Welcome to the Tic-Tac-Toe console game!")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 10")


def attach_signs(player_info):
    signs_information = {}
    sign_1 = input("Please choose a sign: 'X' or 'O': ").upper()
    if sign_1 == "X":
        signs_information[1] = "X"
        signs_information[0] = "O"

    elif sign_1 == "O":
        signs_information[1] = "O"
        signs_information[0] = "X"

    else:
        return False
    return signs_information


def main():
    show_board()
    players = {}
    player_1 = input("First player's name: ")
    player_2 = input("Second player's name: ")
    players[0] = player_2
    players[1] = player_1

    valid_signs = False
    while not valid_signs:
        signs = attach_signs(players)
        if signs:
            valid_signs = True
            main_logic(players, signs)
        else:
            continue


if __name__ == "__main__":
    main()
