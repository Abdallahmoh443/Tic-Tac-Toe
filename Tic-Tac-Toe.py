import random


# Display The Board
def display(board):
    count = 0 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(count != 2 ):
                print(board[i][j],end='  |  ')
                count += 1
            else:
                print(board[i][j],end='')
                count = 0 
        print()


# Check if There Avilable Places in The Board
def avilable_Place(board,place):
    for row in board :
        if(place in row):
            if(row[row.index(place)] not in ('X','O')):
                return True
            else:
                return False

# Check Not Tie 
def check_not_tie(board):
    for i in range(len(board)):
        if('x' not in board[i] and 'o' not in board[i]):
            return True
        else :
            return False

# Check If The Player Win 
def player_win(board):
    counter = 0
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Bottom row
        [(2, 0), (2, 1), (2, 2)],  # Middle row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0,1), (1, 1), (2, 1)],  # Middle column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal
        [(0, 2), (1, 1), (2, 0)]   # Diagonal
    ]
    for condition in win_conditions:
        if all(board[row][col] == 'O' for row, col in condition):
            return True
    return False


# check If player Lose
def player_lose(board):
    counter = 0
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Bottom row
        [(2, 0), (2, 1), (2, 2)],  # Middle row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0,1), (1, 1), (2, 1)],  # Middle column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal
        [(0, 2), (1, 1), (2, 0)]   # Diagonal
    ]
    for condition in win_conditions:
        if all(board[row][col] == 'X' for row, col in condition):
            return True
    return False

def main():
    board = [[1, 2, 3],[4,5,6],[6,8,9]]
    display(board)
    while(check_not_tie(board)):
        print()
        print('**************')
        print()   
        avilable1 = True
        while(avilable1):
            random_place = board[random.randint(0,2)][random.randint(0,2)]
            if(avilable_Place(board,random_place)):
                for row in board :
                    if(random_place in row):
                        row[row.index(random_place)] = 'X'
                        break
                avilable1 = False
        display(board)
        avilable = True  
        while(avilable):
            player = int(input("Entre avilble place : "))
            if(avilable_Place(board,player)):
                for row in board :
                    if(player in row):
                        row[row.index(player)] = 'O'
                avilable = False           
        display(board)
        if(player_win(board)):
            print(' YOU WIN ')
            break
        elif(player_lose(board)):
            print(' YOU LOSE ')
            break 
    else: 
        print(' TIE ')


main()

    
    
 

