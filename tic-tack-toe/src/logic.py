from .helper import is_in_range, is_empty, make_move, check_winner, create_board


def main_logic(players_data, signs):
    player_turn = 1
    matrix = create_board()
    while True:
        print(f"{players_data[player_turn % 2]}'s turn")
        current_move = int(input("Make a move [1:9]: "))
        correct_move = False
        while not correct_move:
            # TODO: Check if the move is in range - DONE
            if is_in_range(current_move):
                # TODO: Check if the slot is empty
                if is_empty(current_move, matrix):
                    correct_move = True
                else:
                    print("Invalid move")
                    current_move = int(input("Make a move [1:9]: "))
                    continue

            else:
                print('Invalid move')
                current_move = int(input("Make a move [1:9]: "))
                continue
        # TODO: Make the move
        make_move(current_move, board=matrix, signs=signs, turn=player_turn)
        if check_winner(matrix):
            print(f"{players_data[player_turn%2]} is the winner!")
            for row in range(len(matrix)):
                print(matrix[row])
            decision = input("Do you want to play again? - [Y / N]: ").upper()
            if decision == "Y":
                main_logic(players_data, signs)
            elif decision == "N":
                exit(0)
        for row in range(len(matrix)):
            print(matrix[row])
        if player_turn > 8:
            print("Tied game!")
            decision = input("Do you want to play again? - [Y / N]: ").upper()
            if decision == "Y":
                main_logic(players_data, signs)
            elif decision == "N":
                exit(0)
        player_turn += 1
