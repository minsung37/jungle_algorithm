import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# DP
dp = [1] * n
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
# ex) 97 98 1 99 2 100 3 4 5 101 102