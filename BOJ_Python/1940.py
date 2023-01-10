N = int(input())
M = int(input())
ids = list(map(int, input().split()))
ids.sort()
front = 0
rear = len(ids)-1
count = 0

while (front != rear):
    if (ids[front]+ids[rear] == M):
        count += 1
        front += 1
    elif (ids[front]+ids[rear] < M):
        front += 1
    else:
        rear -= 1

print(count)
