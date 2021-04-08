import sys
num = 1
for i in range(0, 3):
    num = num*int(sys.stdin.readline().rstrip())
num_list = list(map(int, list(str(num))))
print(num_list.count(0))
print(num_list.count(1))
print(num_list.count(2))
print(num_list.count(3))
print(num_list.count(4))
print(num_list.count(5))
print(num_list.count(6))
print(num_list.count(7))
print(num_list.count(8))
print(num_list.count(9))
