# 문제조건
n, b = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))


# 행렬곱
def product(x, y):
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] = res[i][j] + x[i][k] * y[k][j]

    for i in range(n):
        for j in range(n):
            res[i][j] = res[i][j] % 1000
    return res


# 재귀
def sol(matrix, b):
    if b == 1:
        return matrix
    # 짝수면 제곱하고 = 횟수 절반으로 줄어듦
    elif b % 2 == 0:
        matrix = sol(matrix, b // 2)
        return product(matrix, matrix)
    # 홀수면 나머지를 곱함 횟수 -1
    else:
        matrix = sol(matrix, b - 1)
        return product(matrix, a)


# 정답출력
result = sol(a, b)
for i in range(n):
    for j in range(n):
        print(result[i][j] % 1000, end=" ")
    print()
