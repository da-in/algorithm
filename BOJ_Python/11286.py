from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
pq = PriorityQueue()

for i in range(N):
    n = int(input())
    if (n == 0):
        if (pq.empty()):
            print('0\n')
        else:
            print(str(pq.get()[1])+'\n')
    else:
        pq.put((abs(n), n))
