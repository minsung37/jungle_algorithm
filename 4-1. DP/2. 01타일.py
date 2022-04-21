# n번째 타일 구하기
n = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2

# n번째 타일구하는 점화식
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

# 정답출력
print(dp[n])
