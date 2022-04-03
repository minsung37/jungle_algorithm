import sys
input = sys.stdin.readline

# 문제조건 입력받기
n = int(input())
array = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
answer = []


# 백트래킹
def traking(add, sub, mul, div, res, i):
    # 종료조건
    if add == 0 and sub == 0 and mul == 0 and div == 0:
        # 종료시 answer에 값을 넣고 함수를 종료한다.
        answer.append(res)
        return

    # 재귀호출
    # 각각의 항목이 0이 되면 수행하지 않는다.
    if add:
        traking(add - 1, sub, mul, div, res + array[i], i + 1)
    if sub:
        traking(add, sub - 1, mul, div, res - array[i], i + 1)
    if mul:
        traking(add, sub, mul - 1, div, res * array[i], i + 1)
    if div:
        if res > 0:
            traking(add, sub, mul, div - 1, res // array[i], i + 1)
        else:
            traking(add, sub, mul, div - 1, -(-res // array[i]), i + 1)


# 연산자끼워 넣기
traking(add, sub, mul, div, array[0], 1)
print(max(answer))
print(min(answer))
