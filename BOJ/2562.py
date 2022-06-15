import sys
temp = 0
count = 0
for i in range(0, 9):
    num = int(sys.stdin.readline().rstrip())
    if(num > temp):
        count = i+1
        temp = num
print(temp)
print(count)
