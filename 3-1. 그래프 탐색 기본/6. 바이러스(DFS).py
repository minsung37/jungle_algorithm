import sys
input = sys.stdin.readline

# n : 노드수 m : 연결정보수
computer = int(input())
m = int(input())

# 방문체크
visited = [0] * (computer + 1)

# 인접 행렬로 나타내기
graph = [[0] * (computer + 1) for i in range(computer + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


# dfs
def dfs(v):
    # 방문체크
    visited[v] = 1
    # 재귀적으로 방문
    for i in range(1, computer + 1):
        # 방문 한적이 없고 연결된경우 dfs 호출
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


# 1번 컴퓨터 바이러스 감염
dfs(1)
# 1번 컴퓨터 제외하고 바이러스 감염된 컴퓨터
print(visited.count(1) - 1)