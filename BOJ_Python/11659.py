import sys
input = sys.stdin.readline

N, T = map(int, input().split())

number = list(map(int, input().split()))
sum_number = [0]
for i in range(0, N):
  if(i==0):
    sum_number.append(number[0])
  else:
    sum_number.append(sum_number[i]+number[i])

for j in range(0, T):
  i, j = map(int, input().split())
  print(sum_number[j]-sum_number[i-1])