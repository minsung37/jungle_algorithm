# 정점의수, 장소점보 - 1: 실내, 0: 실외
n = int(input())
place = list(input())

# 방문체크, 인접리스트
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문횟수 담을 변수
count = 0


