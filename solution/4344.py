import sys
n = int(input())
for i in range(0, n):
    score = list(map(int, input().split()))
    avg = (sum(score[1:])/score[0])
    count = 0
    for k in range(1, score[0]+1):
        if(score[k] > avg):
            count = count+1
    print('%.3f' % round(count/score[0]*100, 3) + '%')
