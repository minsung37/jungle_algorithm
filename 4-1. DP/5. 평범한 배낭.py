import sys
input = sys.stdin.readline
# 개수, 제한무게 입력받기
n, k = map(int, input().split())
# DP
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    weight, values = map(int, input().split())
    for j in range(1, k + 1):
        # 가방에 안들어가는 경우 => 이전에 가능한 경우 가져옴
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        # 가방에 들어가는 경우 => 이전꺼랑 바꿔낀거 비교
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + values)
# 정답출력
print(dp[n][k])