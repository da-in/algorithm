import sys

board = []
for i in range(10):
    board.append(list(map(int, sys.stdin.readline().split())))

cur_x = 1
cur_y = 1

while 1 :
    if(board[cur_x][cur_y+1]!=1):
        if(board[cur_x][cur_y+1]==2):
            board[cur_x][cur_y+1]=9
            break
        else:
            board[cur_x][cur_y+1]=9
            cur_y=cur_y+1
    else:
        if(board[cur_x+1][cur_y]==2):
            board[cur_x+1][cur_y]=9
            break
        else:
            board[cur_x+1][cur_y]=9
            cur_x=cur_x+1

for i in range(10):
    for j in range(10):
        print(board[i][j], end="")
        if(j!=9):
            print(" ", end="")
        else:
            print("")