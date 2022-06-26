import sys
n = int(sys.stdin.readline())
xy = []
for i in range(n):
    xy.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,20, 1):
    for j in range(1, 20, 1):
        if([i,j] in xy):
            print("1", end="")
        else:
            print("0", end="")
        if(j!=19):
            print(" ", end="")
        else:
            print("")