# https://www.acmicpc.net/problem/2579(계단오르기)
# 계단 입력받기
n = int(input())
stairs = [0]
for i in range(n):
    a = int(input())
    stairs.append(a)

# DP
if n == 1:
    print(stairs[1])
else:
    # n번째 올랐을때 점수
    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]
    # 계단오르기
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]
    # 정답출력
    print(dp[n])