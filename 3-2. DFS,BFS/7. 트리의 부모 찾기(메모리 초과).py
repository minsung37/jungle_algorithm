import sys
from collections import deque
input = sys.stdin.readline

# 인접 행렬로 구현하면 DFS/BFS 상관없이 메모리 초과
n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

# 연결된곳 1로 표시
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문체크, 부모 노드 저장
visited = [0] * (n + 1)
result = [0] * (n + 1)


# DFS
def dfs(v):
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            result[i] = v
            dfs(i)


# BFS
def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1
                result[i] = v


# 정답출력
bfs(1)
for i in result:
    if i != 0:
        print(i)