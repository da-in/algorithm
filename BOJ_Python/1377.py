import sys
input = sys.stdin.readline
N = int(input())
max = 0
num = []

for i in range(N):
    num.append((int(input()), i))

num.sort()

for j in range(N):
    if (num[j][1]-j > max):
        max = num[j][1]-j

print(max+1)
