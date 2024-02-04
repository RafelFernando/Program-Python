def print_board(value):
    print("\t*******")
    print("\t* {} | {} | {}".format(value[0], value[1], value[2]))
    print("\t* ---|---|---")
    print("\t* {} | {} | {}".format(value[3], value[4], value[5]))
    print("\t* ---|---|---")
    print("\t* {} | {} | {}".format(value[6], value[7], value[8]))
    print("\t*******")

def print_scoreboard(score_board):
    print("\t---")
    print("\tSCOREBOARD")
    print("\t---")
    players = list(score_board.keys())
    print("\t{}\t{}".format(players[0], score_board[players[0]]))
    print("\t{}\t{}".format(players[1], score_board[players[1]]))
    print("\t---\n")

def win_validate(position_player, player_current):
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for combination in win_combinations:
        if all(position in position_player[player_current] for position in combination):
            return True
    return False

def tie_validate(position_player):
    if len(position_player['X']) + len(position_player['O']) == 9:
        return True
    return False

def play_single_game(player_current):
    value = [' ' for _ in range(9)]
    position_player = {'X': [], 'O': []}
    
    while True:
        print_board(value)
        try:
            print("Player {}, it's your turn: ".format(player_current), end="")
            chance = int(input())
        except ValueError:
            print("Invalid input! Please try again.")
            continue

        if chance < 1 or chance > 9 or value[chance - 1] != ' ':
            print("Invalid move! Please try again.")
            continue

        value[chance - 1] = player_current
        position_player[player_current].append(chance)

        if win_validate(position_player, player_current):
            print_board(value)
            print("Congratulations! Player {} wins!".format(player_current))
            return player_current

        if tie_validate(position_player):
            print_board(value)
            print("It's a tie!")
            return 'D'

        player_current = 'O' if player_current == 'X' else 'X'

if __name__ == "__main__":
    print("Enter the name of Player 1:")
    player_first = input("Player 1: ")

    print("Enter the name of Player 2:")
    player_second = input("Player 2: ")

    if player_first.upper() not in ['X', 'O'] or player_second.upper() not in ['X', 'O']:
        print("Invalid name for players. Please use 'X' or 'O'.")
        exit()

    player_current = player_first
    player_choice = {'X': "", 'O': ""}
    option = ['X', 'O']
    score_board = {player_first: 0, player_second: 0}

    print_scoreboard(score_board)

    while True:
        print("{}'s turn".format(player_current))
        print("Press 1 for X")
        print("Press 2 for O")
        print("Press 3 to Exit")

        try:
            choice = int(input())
        except ValueError:
            print("Invalid input! Please try again.\n")
            continue

        if choice == 1:
            player_choice['X'] = player_current
            player_choice['O'] = player_second if player_current == player_first else player_first
        elif choice == 2:
            player_choice['O'] = player_current
            player_choice['X'] = player_second if player_current == player_first else player_first
        elif choice == 3:
            print("Thanks for playing the game!!!")
            print("The final scores are:")
            print_scoreboard(score_board)
            break
        else:
            print("Invalid choice! Please try again.\n")
            continue

        winner = play_single_game(player_current)
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] += 1
            print_scoreboard(score_board)

        player_current = player_second if player_current == player_first else player_first
