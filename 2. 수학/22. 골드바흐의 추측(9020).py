import sys
import math
input = sys.stdin.readline

# 배열의 크기를 선언하고 값을 True로 초기화
limit = 10001
eratos = [True for i in range(limit + 1)]

# 0, 1 제외(False)
eratos[0] = False
eratos[1] = False

# 소수아닌것 제외(False)
for i in range(2, int(math.sqrt(len(eratos)) + 1)):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = False

# 골드바흐 파티션찾기
n = int(input())
for i in range(n):
    a = int(input())
    x = int(a / 2)
    y = a - x
    for j in range(x):
        # 두수 모두 소수인 경우 출력
        if eratos[x] and eratos[y]:
            print(y, x)
            break
        # 아닐경우 1씩 증, 감
        else:
            x = x + 1
            y = y - 1