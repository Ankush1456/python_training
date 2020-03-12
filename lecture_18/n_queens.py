def queens(board, row, n):

    if row == n:
        print("solution mil gaya")
        return

    for col in range(0, n):
        if is_Safe(board, row, col, n):
            board[row][col] = True
            queens(board, row+1, n)
            board[row][col] = False

def is_Safe(board, row, col, n):

    for step in range 

