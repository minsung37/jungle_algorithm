import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

# DP
dp = [0] * len(word2)
for i in range(len(word1)):
    count = 0
    for j in range(len(word2)):
        if count < dp[j]:
            count = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = count + 1

# 정답출력
print(max(dp))