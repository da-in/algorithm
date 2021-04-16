n = int(input())-1
i = 0
while(1):
    n = n-(i*6)
    if(n <= 0):
        print(i+1)
        break
    i = i+1
