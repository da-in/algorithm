# bubble sort
import sys
input = sys.stdin.readline

N = int(input())
num = []
for n in range(N):
    num.append(int(input()))

for i in range(1, N):
    for j in range(0, N-i):
        if (num[j] > num[j+1]):
            num[j], num[j+1] = num[j+1], num[j]

for n in num:
    print(n)
