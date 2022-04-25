import sys
input = sys.stdin.readline


# x로 도달가능한 최고속도 구하기
def max_velocity(x):
    solution = int(((1 + 8 * x) ** 0.5 - 1) // 2) + 1
    return solution


n, m = map(int, input().split())
dp = [[float('inf')] * (max_velocity(n) + 1) for _ in range(n + 1)]
# 1번위치에서 점프시작
dp[1][0] = 0
small_stone = [int(input()) for _ in range(m)]

for location in range(2, n + 1):
    if location in small_stone:
        continue
    # location에서의 최저속도(1)부터 최고속도까지
    for v in range(1, max_velocity(location)):
        # x - 1, x, x + 1 점프뛰기전에 최소점프 횟수 찾기
        dp[location][v] = min(dp[location - v][v - 1],
                              dp[location - v][v],
                              dp[location - v][v + 1]) + 1
# 마지막돌에 방문한적 없는경우
if min(dp[n]) == float('inf'):
    print(-1)
else:
    print(min(dp[n]))
for i in range(len(dp)):
    print(i, dp[i])