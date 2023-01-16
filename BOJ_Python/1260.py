from collections import deque
N, E, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
queue = deque()

# 정렬해야함

for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()


def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for n in graph[v]:
        if (not visited[n]):
            DFS(n)


DFS(start)


def BFS(v):
    visited[v] = True
    queue.append(v)
    print(v, end=' ')
    while (queue):
        cur = queue.popleft()
        for n in graph[cur]:
            if (not visited[n]):
                print(n, end=' ')
                visited[n] = True
                queue.append(n)


print()
visited = [False] * (N+1)
BFS(start)
