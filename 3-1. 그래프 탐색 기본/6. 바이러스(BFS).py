import sys
from collections import deque
input = sys.stdin.readline


# n : 노드수 m : 연결정보수
n = int(input())
m = int(input())

# 방문체크
visited = [0] * (n + 1)

# 인접 행렬로 나타내기
graph = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


# bfs
def bfs(v):
    # 방문할곳 저장
    queue = deque([v])
    # 방문표시
    visited[v] = 1
    # 큐가 빌때까지 반복
    while queue:
        # 방문한거 큐에서 빼기
        v = queue.popleft()
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1


# 1번 컴퓨터 바이러스 감염
bfs(1)
# 1번 컴퓨터 제외하고 바이러스 감염된 컴퓨터
print(visited.count(1) - 1)