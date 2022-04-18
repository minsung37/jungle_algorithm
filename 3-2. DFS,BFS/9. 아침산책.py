import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
path = 0
place = [0] + list(map(int, input().rstrip()))
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]


# 실외 주변에 연결된 실내장소의 개수
def dfs(v, count):
    visited[v] = True
    for i in graph[v]:
        if place[i] == 1:
            count = count + 1
        # 방문안한 실내장소 만난경우
        elif not visited[i] and place[i] == 0:
            count = dfs(i, count)
    return count


for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 연결된 장소 2개가 실내인 경우
    if place[a] == 1 and place[b] == 1:
        # a - b, b - a 두가지 경우
        path = path + 2

# 실외 주변 실내 장소로 경로 카운트
for i in range(1, n + 1):
    # 방문하지 않은 실외
    if not visited[i] and place[i] == 0:
        x = dfs(i, 0)
        path = path + x * (x - 1)

# 정답 출력
print(path)
