import sys
input = sys.stdin.readline

# 행렬 입력받기
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# DP
dp = [[0] * n for _ in range(n)]
for diagonal_row in range(1, n):  # 대각라인 순서
    for row in range(n - diagonal_row):  # 먼저곱하는 행렬
        column = diagonal_row + row  # 뒤에곱하는 행렬, column과 row사이의 차이 1, 2, 3... 순으로 커짐
        dp[row][column] = 2 ** 32
        # 행렬곱해서 작은거 선택하기
        for k in range(row, column):
            dp[row][column] = min(dp[row][column],
                                  dp[row][k] + dp[k + 1][column] + matrix[row][0] * matrix[k][1] * matrix[column][1])
print(dp[0][n - 1])
