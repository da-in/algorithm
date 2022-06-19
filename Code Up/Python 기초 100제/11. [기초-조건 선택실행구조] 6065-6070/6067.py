import sys
num = int(sys.stdin.readline())

if num<0:
    if num%2==0:
        print('A')
    else:
        print('B')
else:
    if num%2==0:
        print('C')
    else:
        print('D')
