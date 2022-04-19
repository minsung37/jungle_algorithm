from collections import deque
import sys
input = sys.stdin.readline

# 이전차수, 연결리스트 만들기
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] = indegree[b] + 1

# 진입차수가 0인 노드를 큐에 삽입
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

# 위상정렬
while queue:
    v = queue.popleft()
    print(v, end=" ")
    for i in graph[v]:
        indegree[i] = indegree[i] - 1
        if indegree[i] == 0:
            queue.append(i)
