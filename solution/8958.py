import sys
n = int(input())
for i in range(0, n):
    score = 0
    total = 0
    results = list(input())
    for result in results:
        if result == 'O':
            score = score+1
            total = total+score
        else:
            score = 0
    print(total)
