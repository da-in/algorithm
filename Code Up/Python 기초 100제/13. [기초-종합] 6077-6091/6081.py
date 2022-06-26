import sys
n = int(sys.stdin.readline(), 16)

for i in range(1,16,1):
    print(f'{format(n, "X")}*{format(i, "X")}={format(n*i, "X")}')