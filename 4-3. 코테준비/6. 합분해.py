n, k = map(int, input().split())
dp = [1] * (n + 1)
for _ in range(k - 1):
    for i in range(1, n + 1):
        dp[i] = dp[i] + dp[i - 1]
    print(dp)
print(dp[-1] % 1000000000)