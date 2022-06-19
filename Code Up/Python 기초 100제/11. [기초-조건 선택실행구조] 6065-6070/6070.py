import sys
n = int(sys.stdin.readline())

n = n%12
if(n<3):
    print('winter')
elif(n<6):
    print('spring')
elif(n<9):
    print('summer')
else:
    print('fall')