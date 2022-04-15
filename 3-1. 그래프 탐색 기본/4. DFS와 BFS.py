import sys
from collections import deque
input = sys.stdin.readline

# 문제 정보 입력받기
n, m, v = map(int, input().split())

# 방문 체크
visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)

# 인접 행렬로 나타내기
graph = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v):
    # 방문한 곳은 1넣기
    visited_dfs[v] = 1
    print(v, end=' ')
    # 재귀적으로 방문
    for i in range(1, n + 1):
        # 방문한 적이 없고, 방문 가능한 경우 dfs실행
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    # 방문할곳 저장
    queue = deque([v])
    # 방문표시
    visited_bfs[v] = 1
    # 큐가 빌때까지 반복
    while queue:
        # 방문한거 큐에서 빼기
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            # 방문한 적이 없고, 방문 가능한 경우 bfs실행
            if visited_bfs[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited_bfs[i] = 1


dfs(v)
print()
bfs(v)