def is_board_full(row1, row2, row3):
    return len([val for val in row1 if val]) == len([val for val in row2 if val]) == len([val for val in row3 if val]) == 3

def is_winner(row1, row2, row3):
    # check to see if anyone won vertically
    if row1[0] == row2[0] == row3[0] != "" or row1[1] == row2[1] == row3[1] != "" or row1[2] == row2[2] == row3[2] != "":
        return True

    # check to see if anyone won horizontally
    if row1[0] == row1[1] == row1[2] != "" or row1[0] == row1[1] == row1[2] != "" or row2[0] == row2[1] == row2[2] != "":
        return True

    # check to see if anyone won diagonally
    if row1[0] == row2[1] == row3[2] != "" or row1[2] == row2[1] == row3[0] != "":
        return True
    
    return False

def display_game_board(row1, row2, row3):
    print(" | ".join(row1))
    print("-------")
    print(" | ".join(row2))
    print("-------")
    print(f"{" | ".join(row3)}\n")

print("Welcome to Tic-Tac-Toe!")
print("Thanks in advance for playing! You may enter the letter 'Q' at any time to exit the game.")

row1, row2, row3 = [["", "", ""] for _ in range(3)]
player_num = 1
while not is_board_full(row1, row2, row3) and not is_winner(row1, row2, row3):

    # display the game board
    print("The game board is currently looks like the following:\n")
    display_game_board(row1, row2, row3)

    # ask one player to make a move. Ask for a row and column number. Add a variable before the loop to indicate whose turn it is next
    print(f"Player {player_num}, enter your next move!")
    while True:
        row_num = input(f"What row number (1, 2 or 3) would you like to place a mark in? ")

        if row_num == 'q' or row_num == 'Q':
            exit(0)

        row_num = int(row_num) - 1
        if 0 <= row_num <= 2:
            break

        print("You entered an invalid row number! Please try again.")
            
    while True:
        col_num = input(f"What column number (1, 2 or 3) would you like to place a mark in? ")

        if col_num == 'q' or col_num == 'Q':
            exit(0)

        col_num = int(col_num) - 1
        if 0 <= col_num <= 2:
            break




# take their guess and update the correct list

# check if the game is over
