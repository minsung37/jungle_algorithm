from collections import deque
import sys
input = sys.stdin.readline

# 문제정보 입력받기
r, s = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
graph_water = [[-1] * s for _ in range(r)]
graph_dochi = [[-1] * s for _ in range(r)]

# 고슴도치, 비버집 좌표
dochi_location = []
home = []

# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 물, 고슴도치 좌표 넣기
queue = deque()

# 비버, 고슴도치 위치 리스트에 넣기, 물 큐에 넣기
for i in range(r):
    for j in range(s):
        # 고슴도치
        if graph[i][j] == 'S':
            dochi_location = [i, j]
            graph_dochi[i][j] = 0
        # 물
        if graph[i][j] == '*':
            queue.append([i, j])
            graph_water[i][j] = 0
        # 비버
        if graph[i][j] == 'D':
            home = [i, j]

# 물차오르기
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < s:
            # 빈곳이고 방문하지 않은 곳 물채우기
            if graph[nx][ny] == "." and graph_water[nx][ny] == -1:
                graph_water[nx][ny] = graph_water[x][y] + 1
                queue.append((nx, ny))

# 고슴도치 비버집으로 이동
queue.append(dochi_location)
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위안에 있고 빈곳이나 비버집이고 방문하지 않은 경우
        if 0 <= nx < r and 0 <= ny < s and graph[nx][ny] in '.DS' and graph_dochi[nx][ny] == -1:
            # 물차는 시간보다 일찍 도착 하는 경우
            if graph_dochi[x][y] + 1 < graph_water[nx][ny] or graph_water[nx][ny] == -1:
                graph_dochi[nx][ny] = graph_dochi[x][y] + 1
                queue.append([nx, ny])

# 정답출력
if graph_dochi[home[0]][home[1]] == -1:
    print('KAKTUS')
else:
    print(graph_dochi[home[0]][home[1]])