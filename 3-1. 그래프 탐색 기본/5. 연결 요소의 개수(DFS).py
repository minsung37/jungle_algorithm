import sys
sys.setrecursionlimit(10**6)
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


# DFS
def dfs(v):
    # 방문한 곳은 1넣기
    visited[v] = 1
    # 재귀적으로 방문
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


# 방문횟수 카운트
count = 0
for i in range(1, n + 1):
    # 방문한 그래프인 경우 재방문 하지 않는다.
    if visited[i] == 0:
        dfs(i)
        count = count + 1
print(count)