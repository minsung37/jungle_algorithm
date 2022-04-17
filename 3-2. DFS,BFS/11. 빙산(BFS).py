from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
year, flag = 0, False
queue = deque()


def bfs(a, b):
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 빙산이 있고 방문 안한경우
                if ice[nx][ny] != 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                # 빙산 녹는 높이 저장
                elif ice[nx][ny] == 0:
                    melt[x][y] = melt[x][y] + 1
    return 1


# 빙산이 분리될때까지 돌아줌
while True:
    result = []
    visited = [[False] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # 바다가 아니고 방문 하지 않은경우
            if ice[i][j] != 0 and not visited[i][j]:
                result.append(bfs(i, j))
    # 빙산을 깍아줌
    for i in range(n):
        for j in range(m):
            ice[i][j] = ice[i][j] - melt[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0
    # 빙산 분리 안되는 경우
    if len(result) == 0:
        break
    # 빙산 2개로 분리된 경우
    if len(result) >= 2:
        flag = True
        break
    year = year + 1

if flag:
    print(year)
else:
    print(0)