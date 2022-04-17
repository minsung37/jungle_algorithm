from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

# 최단 거리 초기화, 출발 도시까지의 거리는 0
distance = [-1] * (n + 1)
distance[x] = 0

# 인접리스트로 만들기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS
queue = deque([x])
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            queue.append(i)

# 정답출력
for i in range(n + 1):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)