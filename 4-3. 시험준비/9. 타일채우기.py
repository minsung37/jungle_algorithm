n = int(input())
# DP
dp = [1] * 16
for i in range(1, 16):
    dp[i] = dp[i - 1] * 3
    dp[i] = dp[i] + 2 * sum(dp[:i - 1])

# 홀수는 타일 못만든다
if n % 2 == 1:
    print(0)
    exit(0)
# 짝수
else:
    print(dp[n // 2])
