"""
In this program I will be replicating the kids game called tic-tac-toe
It will have the option to be played between two people
will use arrays, conditionals, loops, functions and I/O
"""

#---------Global Variables------------

#game board
board =["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

game_still_going = True

winner = None


#Function that displays the current board, by fomrating and printing every element in the array
def display_board(board):
    print(board[0]+"|" + board[1]+ "|" + board[2])
    #print("------")
    print(board[3]+"|" + board[4]+ "|" + board[5])
    #print("------")
    print(board[6]+"|" + board[7]+ "|" + board[8])

    return

#Funtion that is used to run the tic-tac-toe game
#it will combine all the various functions that have been created
#and use them to replicate a game of tic-tac-toe
def play_game():
    display_board(board)


    #while game is still going is True
    while game_still_going:

        player_turn()

        check_if_game_over()


    #The game has ended
    if winner == "X":
        print("Player 1 wins!")
    elif  winner == "O":
            print("Player 2 wins!")
        
    elif winner == None:
        print("Tie.")

    print("Game over")

    return


     


#Asks the users who's turn it is and places their respective "X" or "O" in a valid spot
def player_turn():
    player = input("Enter player number (1 or 2): ")

    #continuously asks the user if its player one or twos turn it is 
    while player not in ["1", "2"]:
        player = input("Invalid input. chose a number from 1-2: ")

    player = int(player)

    
    position = (input("Chose a spot from position 1-9: "))


    #makes sure input is within the range
    while position not in ["1", "2", "3", '4', "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Chocse a position from 1-9: ")
    
    print("Player " + str(player) + "'s turn")

    #adjusts it for array index
    position = int(position) - 1
    
    #makes sure player doesn't try to play on already occupied position
    #checks which player it is and then enters the right char "x" or "o"
    if player == 1:
        if board[position] != "-":
            print("You can't go there Go again.")
        else:
            board[position] = "X"
    else:
        if board[position] != "-":
            print("You can't go there Go again.")
        else:
            board[position] = "O"

    display_board(board)

    return

#checks if the game is over
#calls the functions that check if game is won or a tie
def check_if_game_over():
    check_if_win()
    check_if_tie()

#checks if a player has won the game
def check_if_win():

    global winner 
    # check rows
    row_winner = check_rows()
    # check coloums
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    
    if row_winner:
        winner = row_winner
    
    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return

#checks if a player has won by getting three "x's" or "o's" in a row
def check_rows():

    #if all of the following elements are equal to one another and do not equal "-" then that means that the one player has
    #won the game by connecting all the "o's" or "x's" in that row
    #assigns true or fals to the variable based on that 
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #returns winner (X or 0)

    #if any of the rows are true that means the game has ended
    if row_1 or row_2 or row_3:
        game_still_going = False

    #returns who the winner is "X" or "O" by getting the element from the row that won the game
    if row_1:
        return board[0]

    if row_2:
        return board[3]
    
    if row_2:
        return board[6]
    return

#checks if a player has won by getting three "x's" or "o's" in a column
def check_columns():
    global game_still_going

    #checks if any of the players has won by connecting three in column
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    #if any of the columns are true the game has ended
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    #returns who the winner is "X" or "O" by getting the element from the column that won the game
    if column_1:
        return board[0]

    if column_2:
        return board[1]
    
    if column_2:
        return board[2]

    return

#checks if a player has won by getting three "x's" or "o's" diagonally
def check_diagonals():
    global game_still_going

    #checks if any of the players has won by connecting three in diagonal line
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    #if any of the diagonals are true the game has ended
    if diagonals_1 or diagonals_2:
        game_still_going =False

    #returns who the winner is "X" or "O" by getting the element from the row that won the game
    if diagonals_1:
        return board[0]
    
    elif diagonals_2:
        return board[6]
    
    return

#checks if the game ends in a tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    
    return



print(play_game()) 