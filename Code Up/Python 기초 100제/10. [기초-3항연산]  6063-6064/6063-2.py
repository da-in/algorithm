import sys
a, b = sys.stdin.readline().split()
print(a if int(a)>=int(b) else b)