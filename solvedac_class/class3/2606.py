import sys
input = sys.stdin.readline

com = int(input())
link = int(input())

graph = {}

for i in range(link):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append(b)

    if b not in graph:
        graph[b] = []
    graph[b].append(a)

def dfs(graph, start):
    visited = []
    stack = []

    stack.append(start)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph.get(node, [])))
    
    print(len(visited) - 1)
    return visited

dfs(graph, 1)
