import sys
n = int(input())
nums = []
for i in range(0, n):
    nums.append(int(sys.stdin.readline().rstrip()))
nums = sorted(nums)
for num in nums:
    print(num)
