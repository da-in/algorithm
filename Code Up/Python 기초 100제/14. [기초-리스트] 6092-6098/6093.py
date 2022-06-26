import sys
n = int(sys.stdin.readline())
call = list(map(int,sys.stdin.readline().split()))

for i in range(n, 0, -1):
    if(i==1):
        print(call[i-1], end="")
    else:
        print(call[i-1], end=" ")