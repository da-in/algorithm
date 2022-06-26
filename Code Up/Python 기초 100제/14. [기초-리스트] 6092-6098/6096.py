import sys

xy = []
for i in range(19):
    xy.append(list(map(int, sys.stdin.readline().split())))

n = int(sys.stdin.readline())

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    x=x-1
    y=y-1
    for j in range(19):
        for k in range(19):
            if(j==x and y==k):
                continue
            elif(j==x or y==k):
                xy[j][k]=(xy[j][k]+1)%2

for i in range(19):
    for j in range(19):
        print(xy[i][j], end="")
        if(j!=18):
            print(" ", end="")
        else:
            print("")