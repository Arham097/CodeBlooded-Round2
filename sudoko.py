board = [[0, 0, 0, 0, 4, 0, 0, 2, 6],
[3, 0, 9, 7, 2, 0, 0, 0, 0],
[0, 5, 0, 0, 0, 0, 4, 0, 0],
[0, 0, 7, 9, 1, 3, 0, 0, 0],
[6, 0, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 2],
[1, 0, 0, 0, 0, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 8, 0, 0, 9],
[0, 9, 0, 0, 0, 0, 7, 0, 4]]

# board = [[0, 4, 0, 0, 0, 0, 0, 0, 7],
# [0, 0, 6, 0, 0, 0, 8, 0, 0],
# [0, 0, 0, 3, 0, 4, 1, 0, 0],
# [8, 0, 0, 7, 1, 0, 0, 0, 0],
# [7, 0, 0, 9, 0, 0, 0, 0, 0],
# [5, 6, 2, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 7, 0, 5, 2],
# [0, 0, 0, 0, 2, 0, 0, 0, 0],
# [0, 8, 0, 0, 5, 0, 0, 6, 0]]


# board = [[0, 4, 0, 0, 0, 0, 0, 0, 7],
# [0, 0, 6, 0, 0, 0, 8, 0, 0],
# [0, 0, 0, 3, 0, 4, 1, 0, 0],
# [8, 0, 0, 7, 1, 0, 0, 0, 0],
# [7, 0, 0, 9, 0, 0, 0, 0, 0],
# [5, 6, 2, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 7, 0, 5, 2],
# [0, 0, 0, 0, 2, 0, 0, 0, 0],
# [0, 8, 0, 0, 5, 0, 0, 6, 6]]

def solve_sudoku(board):
    if not is_board_valid(board):
        return False
        
    empty_cell = find_empty(board)
    
    if empty_cell is None:
        return True
        
    row, col = empty_cell
    
    for num in range(1,10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve_sudoku(board) is True:
                return True
                
            # If placing num doesn't lead to solution, backtrack
            board[row][col] = 0  
            
    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print( "---------------------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print( "|", end="")
            
            if board[i][j] == 0:
                print( ". ", end="")
            else:
                print(str(board[i][j]) + " ",end="")
        
        print("\n")

def is_board_valid(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                
                for col in range(9):
                    if col != j and board[i][col] == num:
                        return False
                
                for row in range(9):
                    if row != i and board[row][j] == num:
                        return False
                
                box_row = i // 3
                box_col = j // 3  
                
                for r in range ((box_row * 3),  (box_row * 3 + 3)):
                    for c in range ((box_col * 3),(box_col * 3 + 3)):
                        if (r != i or c != j) and board[r][c] == num:
                            return False
    
    return True

def is_valid(board, num, position):
    row, col = position
    

    for j in range(9):
        if board[row][j] == num and j != col:
            return False
    

    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    

    box_row = row // 3  
    box_col = col // 3  
    
    for i in range ((box_row * 3) , (box_row * 3 + 3)):
        for j in range((box_col * 3) ,(box_col * 3 + 3)):
            if board[i][j] == num and (i, j) != position:
                return False
    
    return True

def find_empty(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  
                return (i, j)
    
    return None


print("Unsolved Board")
print_board(board)



if solve_sudoku(board) is True:
    print ("\nSolved Sudoku:")
    print_board(board)
else:
    print( "\nNo solution exists (puzzle may be invalid or unsolvable).")

