import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]


def tsp(x, visited):
    # 모든 도시를 방문했을때
    if visited == (1 << n) - 1:
        # 출발점으로 가는 경로가 있을 때
        if graph[x][0]:
            return graph[x][0]
        # 출발점으로 가는 경로가 없을 때
        else:
            return INF

    # 이미 최소비용이 계산되어 있다면
    if dp[x][visited] != INF:
        return dp[x][visited]

    # 모든 도시를 탐방
    for i in range(1, n):
        # 가는 경로가 없거나 이미 방문한 도시이면 skip
        if not graph[x][i] or visited & (1 << i):
            continue
        # 점화식
        dp[x][visited] = min(dp[x][visited],
                             tsp(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


print(tsp(0, 1))
# print(n << 1)  # 10을 2배 한 값인 20 이 출력된다.
# print(n >> 1)  # 10을 반으로 나눈 값인 5 가 출력된다.
# [00, 35, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00]
# [00, 00, 00, 25, 00, 00, 00, 18, 00, 00, 00, 15, 00, 00, 00, 00]
# [00, 00, 00, 00, 00, 25, 00, 20, 00, 00, 00, 00, 00, 18, 00, 00]
# [00, 00, 00, 00, 00, 00, 00, 00, 00, 23, 00, 15, 00, 13, 00, 00]