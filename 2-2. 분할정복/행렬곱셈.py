# 행렬A
a, b = list(map(int, input().split()))
matrix_a = []
for _ in range(a):
    matrix_a.append(list(map(int, input().split())))

# 행렬B
matrix_b = []
p, q = list(map(int, input().split()))
for _ in range(p):
    matrix_b.append(list(map(int, input().split())))

# A * B => (a x b) * (p x q) = (a, q) // i-a, j-q, k-b or p (b == p)
# 행렬곱셈
result = [[0 for _ in range(q)] for _ in range(a)]
for i in range(a):
    for j in range(q):
        for k in range(b):
            result[i][j] = result[i][j] + matrix_a[i][k] * matrix_b[k][j]

# 정답 출력
for i in result:
    print(*i)