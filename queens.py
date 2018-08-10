import sys
import time

def create_chessboard(N):
    return [[" □ " for j in range(N)] for i in range(N)]

def print_chessboard(chessboard):
    n = len(chessboard)

    for i in range(n):
        for j in range(n):
            print(chessboard[i][j], end="")
        print(end="\n")

def check_collision(queens, x, y):
    for index, queen in enumerate(queens):
        if queen != -1:
            row = abs(x - index)
            col = abs(y - queen)

            if queen == y or row == col: return True
    else: return False

def set_queen(x, y):
    chessboard[x][y] = " ■ "

def n_queens(queens, row, sols):
    if queens.count(-1) == 0: sols.append(queens[:])

    for col in range(len(queens)):
        collision = check_collision(queens, row, col)

        if not collision:
            queens[row] = col
            n_queens(queens, row + 1, sols)
            queens[row] = -1

if __name__ == "__main__":
    print("N-QUEENS PROBLEM", end="\n\n")

    N = 8

    while(True):
        print("Board size: %d" % N)
        chessboard = create_chessboard(N)
        queens = [-1 for i in range(N)]
        sols = []

        start = time.time()
        n_queens(queens, 0, sols)
        end = time.time()

        print("Total solutions:", len(sols))
        print("Time elapsed", end - start, end="\n")

        for index, queen in enumerate(sols[0]):
            set_queen(index, queen)

        print_chessboard(chessboard)
        N += 1

        print(end="\n")
        input("Press Enter to continue...")
        print(end="\n")
        
