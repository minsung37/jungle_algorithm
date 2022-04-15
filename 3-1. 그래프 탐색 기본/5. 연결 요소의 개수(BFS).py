import sys
from collections import deque
input = sys.stdin.readline

# 문제 정보 입력받기
n, m = map(int, input().split())

# 방문 체크
visited = [0] * (n + 1)

# 인접 행렬로 나타내기
graph = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


# BFS
def bfs(v):
    # 방문 할곳 큐에 저장
    queue = deque([v])
    # 방문한 곳은 1넣기
    visited[v] = 1
    # 큐가 빌때까지 반복
    while queue:
        # 방문한거 큐에서 빼기
        v = queue.popleft()
        for i in range(1, n + 1):
            # 방문한 적이 없고, 방문 가능한 경우 bfs실행
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1


# 방문횟수 카운트
count = 0
for i in range(1, n + 1):
    # 방문한 그래프인 경우 재방문 하지 않는다.
    if visited[i] == 0:
        bfs(i)
        count = count + 1
print(count)