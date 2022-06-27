import sys
h, w = map(int, sys.stdin.readline().split())
board = []
for i in range(h):
    row = []
    for i in range(w):
        row.append(0)
    board.append(row)

n = int(sys.stdin.readline())
for i in range(n):
    l, d, x, y = map(int, sys.stdin.readline().split())
    x=x-1
    y=y-1
    if(d==0):
        # 가로
        for j in range(l):
            board[x][y+j]=(board[x][y+j]+1)%2
    else:
        # 세로
        for j in range(l):
            board[x+j][y]=(board[x+j][y]+1)%2

for i in range(h):
    for j in range(w):
        print(board[i][j], end="")
        if(j!=w-1):
            print(" ", end="")
        else:
            print("")