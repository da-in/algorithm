import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0


def dfs(v):
    visited[v] = True
    for n in graph[v]:
        if (not visited[n]):
            dfs(n)


for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, N+1):
    if (not visited[j]):
        count += 1
        dfs(j)

print(count)
