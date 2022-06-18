import sys
num = list(map(int, sys.stdin.readline().split()))

for n in num :
    if(n%2==0):
        print('even')
    else:
        print('odd')

