import sys
input = sys.stdin.readline

# 문제조건 입력받기
n = int(input())
array = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
answer = []


def sol(add, sub, mul, div, result, i):
    if add == 0 and sub == 0 and mul == 0 and div == 0:
        answer.append(result)
        return
    if add:
        sol(add - 1, sub, mul, div, result + array[i], i + 1)
    if sub:
        sol(add, sub - 1, mul, div, result - array[i], i + 1)
    if mul:
        sol(add, sub, mul - 1, div, result * array[i], i + 1)
    if div:
        if result > 0:
            sol(add, sub, mul, div - 1, result // array[i], i + 1)
        else:
            sol(add, sub, mul, div - 1, -(-result) // array[i], i + 1)


sol(add, sub, mul, div, array[0], 1)
print(max(answer))
print(min(answer))