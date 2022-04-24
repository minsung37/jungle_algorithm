import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()
n, m = len(word1), len(word2)

# DP
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 끝에 추가된 문자를 비교
        # 같은경우
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 다른경우
        else:
            # 인접한 경우에서 가장 문자열 고르기
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
# 정답출력
print(dp[-1][-1])