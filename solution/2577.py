import sys
num = 1
for i in range(0, 3):
    num = num*int(sys.stdin.readline().rstrip())
num_list = list(map(int, list(str(num))))
for i in range(0, 10):
    print(num_list.count(i))
