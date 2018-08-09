SOLUTION = []
N = 8

def check_collision(queens, x, y):
    for index, queen in enumerate(queens):
        if queen != -1:
            row = abs(x - index)
            col = abs(y - queen)

            if queen == y or row == col: return True
    else: return False

def set_queen_chessboard(x, y):
    chessboard[x][y] = " ■ "

def print_chessboard(chessboard):
    n = len(chessboard)

    print(end="\n   ")
    [print(" %d " % i, end="") for i in range(n)]
    print(end="\n")

    for i in range(n):
        print(" %d " % (i), end="")
        for j in range(n):
            print(chessboard[i][j], end="")
        print(end="\n")

def create_chessboard():
    return [[" □ " for j in range(N)] for i in range(N)]

def eight_queens(queens, row):
    if queens.count(-1) == 0: SOLUTION.append(queens[:])

    for col in range(N):
        collision = check_collision(queens, row, col)

        if not collision:
            queens[row] = col
            eight_queens(queens, row + 1)
            queens[row] = -1

if __name__ == "__main__":
    chessboard = create_chessboard()
    queens = [-1 for i in range(N)]

    eight_queens(queens, 0)

    print('N-QUEENS PROBLEM')
    print('Total solutions: ', len(SOLUTION))

    for index, queen in enumerate(SOLUTION[0]):
        set_queen_chessboard(index, queen)

    print_chessboard(chessboard)
