# https://www.acmicpc.net/problem/1389
from collections import deque
import sys
input = sys.stdin.readline

# 유저수, 친구관계수
n, m = map(int, input().split())
# 친구관계 만들기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# BFS
def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)


# 친구탐색, 정답출력
kbn = []
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    kbn.append(sum(visited))
print(kbn.index(min(kbn)) + 1)