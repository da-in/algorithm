import sys
input = sys.stdin.readline
num_len, rep = map(int, input().split())
numbers = list(map(int, input().split()))
pre_sum = [0]
temp = 0

for num in numbers:
  temp = temp + num
  pre_sum.append(temp)

for i in range (rep):
  s, e = map(int, input().split())
  print(pre_sum[e]-pre_sum[s-1])