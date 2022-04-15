import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
# 방문체크, 부모 노드 저장
visited, result = [0] * (n + 1), [0] * (n + 1)

# 인접 리스트로 만들기 => 인접행렬은 메모리초과
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# DFS
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            result[i] = v
            dfs(i)
    return


# 정답출력
dfs(1)
for i in range(2, n + 1):
    print(result[i])
