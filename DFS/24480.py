import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

count = 0 
def dfs(graph, visited, start):
    global count
    count += 1
    visited[start] = count
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i)

n, m, r = map(int, input().split())

visited = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

dfs(graph, visited, r)

for i in range(1, n + 1):
    if visited[i] != 0:
        print(visited[i])
    else:
        print(0)
