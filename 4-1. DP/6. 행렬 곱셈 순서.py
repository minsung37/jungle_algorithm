# 행렬 입력받기
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# DP
dp = [[0] * n for _ in range(n)]
for i in range(1, n):  # i는 간격에 따른 대각선 줄을 의미한다.
    for j in range(n - i):  # j는 대각선의 항목들
        x = i + j
        dp[j][x] = 2 ** 32
        for k in range(j, x):  # 나올 수 있는 모든 최솟값을 구한다.
            print(j, k)
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])
        for z in dp:
            print(*z)
        print()
print(dp[0][n - 1])
