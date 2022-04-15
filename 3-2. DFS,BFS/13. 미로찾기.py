from collections import deque

# 미로정보 입력받기
n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

# 방향설정
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 거를조건
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if miro[nx][ny] == 1:
                queue.append((nx, ny))
                # 방문하는 점에 지나온 칸수를 더해서 기록함
                miro[nx][ny] = miro[x][y] + 1
    return miro[n - 1][m - 1]