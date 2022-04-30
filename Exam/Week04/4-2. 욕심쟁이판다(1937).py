# https://www.acmicpc.net/problem/1937(욕심쟁이판다)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

# 맵전보, 방문체크, 방향
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited, result = [[0] * n for _ in range(n)], 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


# DFS
def dfs(x, y):
    if visited[x][y] != 0:
        return visited[x][y]
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 칸안에 있을떄
        if 0 <= nx < n and 0 <= ny < n:
            # 다음칸수에 많을때 방문하거나 유지하거나
            if graph[x][y] < graph[nx][ny]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)
    return visited[x][y]


for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
print(result)