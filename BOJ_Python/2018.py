N = int(input())
count = 0
start = 1
end = 1
temp = 1

while (start < N):
    if (temp <= N):
        if (temp == N):
            count += 1
        end += 1
        temp += end
    else:
        temp -= start
        start += 1

print(count+1)
