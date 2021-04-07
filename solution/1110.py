N = int(input())
n = N
cnt = 0
while(1):
    a = n//10
    b = n % 10
    c = (b*10) + ((a+b) % 10)
    cnt = cnt+1
    n = c
    if (c == N):
        print(cnt)
        break
