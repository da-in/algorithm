n, x = map(int, input().split())
temp = input().split()
for i in range(0, n):
    if(int(temp[i]) < x):
        print(temp[i], end=' ')
