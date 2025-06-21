import sys
input = sys.stdin.readline

vertex, edge, start = map(int, input().split())

graph = {}

for i in range(edge):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

    if v not in graph:
        graph[v] = []
    graph[v].append(u)

def bfs(graph, start):
    visited = []
    stack = []

    stack.append(start)
    while len(stack) != 0:
        stack.sort()
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph.get(node, [])))
            print(node, end='\n')
        if len(stack) == 0:
            print(0)
    return visited

bfs(graph, start)