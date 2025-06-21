#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_V 1001

int N, M, V;
int visited[MAX_V];
int graph[MAX_V][MAX_V];

void dfs(int v) {
    visited[v] = 1;
    printf("%d ", v);
    for (int i = 1; i <= N; i++) {
        if (graph[v][i] && !visited[i]) {
            dfs(i);
        }
    }
}

void bfs(int start) {
    int queue[MAX_V], front = 0, rear = 0;
    visited[start] = 1;
    queue[rear++] = start;

    while (front < rear) {
        int v = queue[front++];
        printf("%d ", v);
        for (int i = 1; i <= N; i++) {
            if (graph[v][i] && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    scanf("%d %d %d", &N, &M, &V);
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u][v] = graph[v][u] = 1;
    }

    memset(visited, 0, sizeof(visited));
    dfs(V);
    printf("\n");

    memset(visited, 0, sizeof(visited));
    bfs(V);
    printf("\n");

    return 0;
}
