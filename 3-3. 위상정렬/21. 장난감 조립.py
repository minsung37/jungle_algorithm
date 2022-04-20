import sys
from collections import deque
input = sys.stdin.readline

# 연결정보, 필요푸품, 이전차수
n = int(input())
graph = [[] for _ in range(n + 1)]
parts = [[0] * (n + 1) for _ in range(n + 1)]
indrgree = [0] * (n + 1)
queue = deque()

# 연결정보, 이전차수
for _ in range(int(input())):
    a, b, cost = map(int, input().split())
    graph[b].append((a, cost))
    indrgree[a] = indrgree[a] + 1

# 진입차수가 0인 노드를 큐에 삽입
for i in range(1, n + 1):
    if indrgree[i] == 0:
        queue.append(i)

# 위상 정렬 시작
while queue:
    now = queue.popleft()
    # 현 부품의 다음 단계, 현 부품의 필요량
    for next, next_parts in graph[now]:
        # 현 푸품이 기본 부품이면
        if parts[now].count(0) == n + 1:
            # 다음 부품에 지금 부품의 수를 더함
            parts[next][now] = parts[next][now] + next_parts
        # 현 제품이 중간 부품이면
        else:
            for i in range(1, n + 1):
                parts[next][i] = parts[next][i] + parts[now][i] * next_parts
        # 차수 다운
        indrgree[next] = indrgree[next] - 1
        if indrgree[next] == 0:
            # 차수 0이면 큐에 넣음
            queue.append(next)
for x in enumerate(parts[n]):
    if x[1] > 0:
        print(*x)
for i in parts:
    print(i)