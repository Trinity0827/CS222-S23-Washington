def print_board(board):
    for row in board:
        print (" ".join("Q" if x else " . " for x in row))
    

if __name__ == "__main__":
    N = 5 # chnage N to the desired board size
    solve_nqueens(N)
    