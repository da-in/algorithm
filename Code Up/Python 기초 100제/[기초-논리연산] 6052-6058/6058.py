import sys
a, b = sys.stdin.readline().split()
print(not(bool(int(a))|bool(int(b))))