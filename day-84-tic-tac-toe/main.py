def is_board_full(row1, row2, row3):
    return len([val for val in row1 if val != " "]) == len([val for val in row2 if val != " "]) == len([val for val in row3 if val != " "]) == 3

def is_winner(row1, row2, row3):
    # check to see if anyone won vertically
    if row1[0] == row2[0] == row3[0] != " " or row1[1] == row2[1] == row3[1] != " " or row1[2] == row2[2] == row3[2] != " ":
        return True

    # check to see if anyone won horizontally
    if row1[0] == row1[1] == row1[2] != " " or row1[0] == row1[1] == row1[2] != " " or row2[0] == row2[1] == row2[2] != " ":
        return True

    # check to see if anyone won diagonally
    if row1[0] == row2[1] == row3[2] != " " or row1[2] == row2[1] == row3[0] != " ":
        return True
    
    return False

def display_game_board(row1, row2, row3):
    print(" | ".join(row1))
    print("---------")
    print(" | ".join(row2))
    print("---------")
    print(f"{" | ".join(row3)}\n")

def get_user_input(row_or_column):
    while True:
        num = input(f"What {row_or_column} number (1, 2 or 3) would you like to place a mark in? ").upper()

        if num == 'Q':
            print("Thanks for playing! I hope you will play again soon.")
            exit(0)

        try:
            num = int(num) - 1
        except ValueError:
            print(f"You entered an invalid {row_or_column} number! Please try again.")
            continue
       
        if 0 <= num <= 2:
            return num
        else:
            print(f"You entered an invalid {row_or_column} number! Please try again.")

print("Welcome to Tic-Tac-Toe! Player 1 will be 'X' on the board, while player 2 will be 'O'.")
print("You may enter the letter 'Q' at any time to exit the game.")

row1, row2, row3 = [[" ", " ", " "] for _ in range(3)]
player_num = 1
while not is_board_full(row1, row2, row3):

    # display the game board
    print("\nThe game board currently looks like the following:\n")
    display_game_board(row1, row2, row3)

    # ask one player to make a move. Ask for a row and column number.
    print(f"Player {player_num}, enter your next move!")
    row_num_index = get_user_input("row")
    col_num_index = get_user_input("column")

    is_spot_already_taken = eval(f"row{row_num_index + 1}[{col_num_index}] != ' '")
    if is_spot_already_taken:
        print("The spot you entered is already taken! Please try again.")
        continue

    exec(f"row{row_num_index + 1}[{col_num_index}] = '{"X" if player_num == 1 else "O"}'")

    if is_winner(row1, row2, row3):
        print("\nThe game board currently looks like the following:\n")
        display_game_board(row1, row2, row3)
        print(f"Congratulations, player {player_num}! You won!")
        break

    player_num = 3 - player_num
