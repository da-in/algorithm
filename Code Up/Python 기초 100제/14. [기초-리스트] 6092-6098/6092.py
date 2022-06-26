import sys
n = int(sys.stdin.readline())
call = list(map(int,sys.stdin.readline().split()))
res = []
for i in range(23):
    res.append(0)

for i in call:
    res[i-1] = res[i-1]+1

for i in range(23):
    if(i==22):
        print(res[i], end="")
    else:
        print(res[i], end=" ")