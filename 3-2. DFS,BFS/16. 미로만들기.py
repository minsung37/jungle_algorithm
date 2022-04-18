from collections import deque
import sys
input = sys.stdin.readline

# 미로 입력받기
n = int(input())
miro = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

# 방향 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS
queue = deque()
queue.append((0, 0))
visited[0][0] = 0
while queue:
    x, y = queue.pop()
    # 미로 우측하단에 도달한 경우
    if x == n - 1 and y == n - 1:
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 방문 한적 없고
            if visited[nx][ny] == -1:
                # 벽인 경우
                if miro[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    # 벽을 우선적으로 탐색
                    queue.appendleft((nx, ny))
                # 길인 경우
                else:
                    visited[nx][ny] = visited[x][y]
                    queue.append((nx, ny))