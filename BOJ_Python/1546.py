N = int(input())
scores =list(map(int, input().split()))
print(sum(scores) / N / max(scores) * 100)