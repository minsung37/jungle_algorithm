from collections import deque
import sys
input = sys.stdin.readline

# 토마토 정보입력받기
m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

# 토마토가 익는 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 토마토 좌표를 큐에 넣기
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

# BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 토마토 상자 범위안에 있고
        if 0 <= nx < n and 0 <= ny < m:
            # 토마토가 익지 않은 상태일때
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

# 정답 출력
day = []
for i in tomato:
    if 0 in i:
        print(-1)
        exit(0)
    day.append(max(i))
print(max(day) - 1)