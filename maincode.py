# Tic Tack Toe - Learning Python 101

def main():
    # The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)  # +function that starts the game.


def intro():
    # function to introduce the rules
    print("Tic Tac Toe!")
    print("\n")
    print("Rules: P1 and P2, represented by X and O, take turns, marking the spaces in a 3*3 grid.")
    print("\n")
    print("Player picks a row "
                    "[0:2]"
          " and then a column "
                    "[0:2]")
    print("\n")
    print("The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue ...")
    print("\n")


def create_grid():
    # function to create a blank playboard
    print(" ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def sym():
    # function to decide the players' symbols
    symbol_1 = input("Player 1, choose X or O? \n ")

    if symbol_1 == "X" or "x":
        symbol_2 = "O"
        print("Welcome...\n Player 1 you are X \n Player 2 you are O")
    if symbol_1 == "O" or "o":
        symbol_2 = "X"
        print("Welcome...\n Player 1 you are O \n Player 2 you are X")
    else:
        symbol_2 = "X"
        print("Welcome...\n Player 1 you are O \n Player 2 you are X \n")
    input("Press enter to Start.")
    print("\n")
    return (symbol_1, symbol_2)


def startGamming(board, symbol_1, symbol_2, count):
    # function which starts the game.

    # Decides the turn
    if count % 2 == 1:
        player = symbol_1
    elif count % 2 == 0:
        player = symbol_2
    print( player + ", goes first! ")
    row = int(input("Pick a row: "))
    column = int(input("Pick a column: "))

    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row:"))
        column = int(input("Pick a column:"))

        # Check if the square is already filled
    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row:"))
        column = int(input("Pick a column:"))

        # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1

    else:
        board[row][column] = symbol_2

    return (board)


def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    # This function check if the board is full
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)

        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("Everyone's a Winner!")

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")

    # This is function gives a report
    report(count, winner, symbol_1, symbol_2)


def outOfBoard(row, column):
    # This function tells the players that their selection is out of range
    print("Out of boarder. Pick choose again. ")


def printPretty(board):
    # function prints the board
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board


def isWinner(board, symbol_1, symbol_2, count):
    # This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", Whoop! You won!")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you are the winner :)")

    # Check the columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", Congrats you won!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", is the winner!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", Wins!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", is the winner!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", is the winner!")

    return winner


def illegal(board, symbol_1, symbol_2, row, column):
    print("Pick another one.")


def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1):
        print("Winner : Player " + symbol_1)
        print("2nd Place: Player "+ symbol_2)
    elif (winner == False) and (count % 2 == 0):
        print("Winner : Player " + symbol_2)
        print("2nd Place: Player " + symbol_1)
    else:
        print("Nobody loses :)")


# Call Main
main()

