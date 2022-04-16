from collections import deque
import sys
input = sys.stdin.readline

# 토마토 정보입력받기
m, n, v = map(int, input().split())
tomato = []
for _ in range(v):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    tomato.append(temp)

# 토마토가 익는 방향
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 토마토 좌표를 큐에 넣기
queue = deque()
for i in range(n):
    for j in range(m):
        for k in range(v):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j))

# BFS
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        # 토마토 상자 범위안에 있고
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < v:
            # 토마토가 익지 않은 상태일때
            if tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append((nz, nx, ny))

# 정답출력
day = []
temp = []
for i in tomato:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
        temp.append(max(j))
    day.append(max(temp))
print(max(day) - 1)