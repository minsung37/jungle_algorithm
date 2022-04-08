import sys
input = sys.stdin.readline


# 시작도시번호, 다음도시번호, 비용, 방문 도시
def dfs(start, end, value, visited):
    global cost
    # 모두 방문 했을때, 다시 시작점으로 돌아 갈 수 있는경우
    if len(visited) == n and graph[end][start] != 0:
        # 최소비용 갱신
        cost = min(cost, value + graph[end][start])
        return
    for i in range(n):
        # 방문가능, 방문한적x, 현재까지비용이 최소보다 작아야함
        if graph[end][i] != 0 and i not in visited and value < cost:
            visited.append(i)
            dfs(start, i, value + graph[end][i], visited)
            visited.pop()


# 문제조건 입력받기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cost = 999999999
for i in range(n):
    dfs(i, i, 0, [i])
print(cost)
