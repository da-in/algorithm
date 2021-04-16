n = int(input())
i = 0
while(1):
    i = i+1
    if(n <= i):
        if(i % 2 == 0):
            print(f'{n}/{i-n+1}')
        else:
            print(f'{i-n+1}/{n}')
        break
    else:
        n = n-i
