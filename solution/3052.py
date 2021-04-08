import sys
num_list = set()
for i in range(0, 10):
    num_list.add(int(sys.stdin.readline().rstrip()) % 42)
print(len(num_list))
