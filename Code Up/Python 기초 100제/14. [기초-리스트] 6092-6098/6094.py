import sys
n = int(sys.stdin.readline())
call = list(map(int,sys.stdin.readline().split()))
temp = call[0]
for num in call:
    if(temp>num):
        temp=num
print(temp)