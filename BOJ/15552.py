import sys
a = int(sys.stdin.readline().rstrip())
for i in range(0, a):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
