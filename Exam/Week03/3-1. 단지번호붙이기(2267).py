# https://www.acmicpc.net/problem/2667
from collections import deque
import sys
input = sys.stdin.readline

# n 입력받기
n = int(input())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

# 방향설정
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1
    # 큐가 빌때까진 반복
    while queue:
        x, y = queue.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 방문한경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count = count + 1
    return count


# 모든 노드(위치)에 대하여 탐색
array = []
for i in range(n):
    for j in range(n):
        # 현재 위치에서 BFS 수행
        # 단지가 구해진경우
        if graph[i][j] == 1:
            # 현재까지 단지수 array에 저장
            array.append(bfs(i, j))

# 정답출력
array.sort()
print(len(array))
for i in range(len(array)):
    print(array[i])