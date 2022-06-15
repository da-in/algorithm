import sys
n = int(input())
count = 0
for i in range(0, n):
    word = sys.stdin.readline().rstrip()
    a = len(set(word))
    b = 0
    temp = ''
    for c in word:
        if c!=temp:
            b=b+1
        temp = c
    if a==b:
        count=count+1
    
print(count)