import time

def instructions():
    print("Welcome to the game!")
    time.sleep(1)  # Delay for 1 second
    print("Here's how to play:")
    time.sleep(1)
    print("1. The game board consists of 9 positions, numbered from 1 to 9.")
    time.sleep(1)
    print("2. Players take turns to place their mark on the board.")
    time.sleep(1)
    print("3. The first player will use 'X' and the second player will use 'O'.")
    time.sleep(1)
    print("4. To place your mark, enter the number corresponding to the position on the board.")
    time.sleep(1)
    
def move(board, player):
    """
    Asks the current player to enter their desired position and updates the board.

    Parameters:
    board (list): The current state of the board as a list of strings.
    player (str): The current player's mark ('X' or 'O').

    Returns:
    list: The updated board.
    """
    while True:
        try:
            # Ask the player for their desired position
            position = int(input(f"Player {player}, enter your desired position (1-9): "))
            
            # Validate the position
            if position < 1 or position > 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
            
            # Convert the position to zero-based index
            index = position - 1
            
            # Check if the position is available
            if board[index] not in ['X', 'O']:
                # Place the player's mark on the board
                board[index] = player
                break
            else:
                print("Position already taken. Please choose another position.")
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    
    return board

# Example usage:
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player = 'X'

# Call the move function to update the board
updated_board = move(board, player)

print("Updated board:")
print(updated_board)    