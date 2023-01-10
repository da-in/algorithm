import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
count = 0


def isGoodNumber(i):
    n = num_list[i]
    front = 0
    rear = len(num_list)-1
    while (front < rear):
        if (num_list[front]+num_list[rear] == n):
            if (front == i):
                front += 1
            elif (rear == i):
                rear -= 1
            else:
                return 1
        elif (num_list[front]+num_list[rear] < n):
            front += 1
        else:
            rear -= 1
    return 0


for i in range(len(num_list)):
    count += isGoodNumber(i)

print(count)
