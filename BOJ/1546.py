n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
print(sum(score)/len(score)/max_score*100)
