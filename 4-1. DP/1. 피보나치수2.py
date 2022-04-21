# n번째 피보나치수 구하기
n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

# 피보나치수 구하는 점화식
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

# 정답출력
print(dp[-1])
