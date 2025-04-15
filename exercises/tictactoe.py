# Defining functions
def player():
    acceptable_values = ["X", "O"]
    answer = False

    while answer == False:
        player1 = input("Player 1: Do you want to be X or O? ")

        if player1 in acceptable_values:
            answer == True
            print("Player 1 will go first.")
            return player1


def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def get_index(counter):
    answer = False

    if (counter % 2) == 0:
        current_player = "Player 1"
    else:
        current_player = "Player 2"

    while answer == False:
        index = input(f"{current_player}: Choose a position on the board (1-9) ")

        if index in board and index.isdigit() == True:
            answer = True
            return int(index), current_player
        else:
            print("Please enter a valid position.")


def full_board(board):
    for item in board:
        if item not in ["X", "O"]:
            return False
    
    return True

def play_again():
    acceptable_values = ["Y", "N"]
    answer = False
    
    while answer == False:
        result = input("Do you want to play again? (Y/N)  ")
        if result in acceptable_values:
            answer = True
            if result == "Y":
                return True
            else:
                return False

def check_winner(board, char):

    winning_combinations = [ 
        (0,1,2), 
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6) 
    ]

    for a,b,c in winning_combinations:
        if board[a] == board[b] == board[c] == char:
            return True
    
    return False

   
# Print out welcome message
print("Welcome to Tic Tac Toe!")

# Store which char player 1 uses
XorO = player()

# Sets up default layout for board
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Shows board to players
display_board(board)

# Start game
game_on = True
counter = 0

while game_on:

    # Ask current player for index on board
    index,current_player = get_index(counter)

    # Determine which char to use for current player
    acceptable_chars = ["X", "O"]
    if (counter % 2) == 0: 
        current_char = XorO
    else:
        current_char = (set(["X", "O"]) - {XorO}).pop() 

    # Update board layout   
    board[index - 1] = current_char

    # Display new board layout
    display_board(board)

    counter += 1

    # Check if someone has three in a row
    if check_winner(board, current_char):
        print(f"{current_player} has won the game!")

        # Check if the player wants to play again
        game_on = play_again()
        if game_on:
            XorO = player()
            counter = 0
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            display_board(board)
        else:
            print("Thanks for playing!")

    # Check if the whole board is full
    if full_board(board):
        print("You have tied!")
        
        # Check if the player wants to play again
        game_on = play_again()
        if game_on:
            XorO = player()
            counter = 0
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            display_board(board)
        else:
            print("Thanks for playing!")
            

            


 



