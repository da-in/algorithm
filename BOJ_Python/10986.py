N, M = map(int, input().split())
count = 0
number = list(map(int, input().split()))
prefix_sum_remainder = [0]
remainder_count = [0]*M

for i in range(1, N+1):
    temp = (prefix_sum_remainder[i-1]+number[i-1]) % M
    prefix_sum_remainder.append(temp)
    if (temp == 0):
        count += 1
    remainder_count[temp] += 1

for rc in remainder_count:
    count += (rc * (rc-1))//2

print(count)
