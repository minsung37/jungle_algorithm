import sys
import math
input = sys.stdin.readline

# 배열의 크기를 선언하고 값을 True로 초기화
limit = 1000001
eratos = [True for i in range(limit + 1)]

# 0, 1 제외(False)
eratos[0] = False
eratos[1] = False

# 소수아닌것 제외(False)
for i in range(2, int(math.sqrt(len(eratos)) + 1)):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = False

# 골드바흐 파티션
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, limit):
        if eratos[i] and eratos[n - i]:
            print(n, "=", i, "+", n - i)
            break
    else:
        print("Goldbach's conjecture is wrong")