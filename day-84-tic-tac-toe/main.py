def is_board_full(rows):
    for row in rows:
        for value in row:
            if value == " ":
                return False
    return True

def is_winner(rows):
    for num in range(3):
        # check to see if anyone won vertically
        if rows[0][num] == rows[1][num] == rows[2][num] != " ":
            return True
        
        # check to see if anyone won horizontally
        if rows[num][0] == rows[num][1] == rows[num][2] != " ":
            return True
        
    # check to see if anyone won diagonally
    if rows[0][0] == rows[1][1] == rows[2][2] != " " or rows[0][2] == rows[1][1] == rows[2][0] != " ":
        return True
    
    return False

def display_game_board(rows):
    for num in range(2):
        print(" | ".join(rows[num]))
        print("---------")
    print(f"{' | '.join(rows[2])}\n")


def get_user_move(row_or_column):
    while True:
        num = input(f"What {row_or_column} number (1, 2 or 3) would you like to place a mark in? ").upper()

        if num == 'Q':
            print("Thanks for playing! I hope you will play again soon.")
            exit(0)

        try:
            num = int(num)
        except ValueError:
            print(f"You entered an invalid {row_or_column} number! Please try again.")
            continue
       
        if 1 <= num <= 3:
            return num
        else:
            print(f"You entered an invalid {row_or_column} number! Please try again.")

def is_spot_already_taken(rows, row_input, col_input):
    return rows[row_input - 1][col_input - 1] != " "

def get_user_input_for_continuing():
    response = input("Would you like to play again? Type 'Y' or 'N'. ").upper()
    
    if response == "Y" or response == "N":
        return response
    
    print("You entered an invalid response! Please try again.")
    get_user_input_for_continuing()

def play_game():
    print("Welcome to Tic-Tac-Toe! Player 1 will be 'X' on the board, while player 2 will be 'O'.")
    print("You may enter the letter 'Q' at any time to exit the game.")

    while True:
        rows = [[" ", " ", " "] for _ in range(3)]
        player_num = 1

        while True:

            # display the game board
            print("\nThe game board currently looks like the following:\n")
            display_game_board(rows)

            if is_winner(rows):
                print(f"Congratulations, player {3 - player_num}! You won!")
                break

            if is_board_full(rows):
                print(f"It's a tie! The board is full.")
                break

            # ask one player to make a move. Ask for a row and column number.
            print(f"Player {player_num}, enter your next move!")
            row_num = get_user_move("row")
            col_num = get_user_move("column")

            if is_spot_already_taken(rows, row_num, col_num):
                print("The spot you entered is already taken! Please try again.")
                continue

            rows[row_num - 1][col_num - 1] = "X" if player_num == 1 else "O"
            player_num = 3 - player_num

        if get_user_input_for_continuing() == "N":
            print("Thanks for playing! I hope you will play again soon.")
            break


if __name__ == "__main__":
    play_game()
