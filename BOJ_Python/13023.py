import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N)]
visit = [False] * (N)
answer = 0

for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def DFS(v, depth):
    if (depth == 4):
        return 1
    visit[v] = True
    for n in graph[v]:
        if (not visit[n]):
            print('DFS(', n, depth+1, ')')
            if (DFS(n, depth+1)):
                return 1
    visit[v] = False
    return 0


for i in range(N):
    visit = [False] * (N)
    print('DFS(', i, 0, ')')
    if (DFS(i, 0)):
        answer = 1
        break

print(answer)
