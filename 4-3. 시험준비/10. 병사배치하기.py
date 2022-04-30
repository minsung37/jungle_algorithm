import sys
input = sys.stdin.readline

# 가장긴 감소하는 부분 수열
n = int(input())
array = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))