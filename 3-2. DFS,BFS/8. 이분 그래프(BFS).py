import sys
from collections import deque
input = sys.stdin.readline


# BFS
def bfs(x):
    global result
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        v = queue.popleft()
        # v에 연결된 점 방문
        for i in graph[v]:
            # 방문한적 없으면 방문
            if visited[i] == 0:
                # 방문표시 교차로 표기
                visited[i] = visited[v] % 2 + 1
                queue.append(i)
            else:
                # 이전 방문했던 그래프와 방문표시가 같으면
                if visited[i] == visited[v]:
                    result = "NO"
                    return


k = int(input())
for _ in range(k):
    # 정점개수, 간선개수 입력받기
    v, e = map(int, input().split())
    # 방문체크
    visited = [0] * (v + 1)
    # 인접리스트 만들기
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 이분 그래프 여부
    result = "YES"
    for i in range(1, v + 1):
        # 방문한적 없고 현재까지 이분그래프일때
        if visited[i] == 0 and result == "YES":
            bfs(i)
    print(result)