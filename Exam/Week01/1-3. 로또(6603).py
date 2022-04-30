# https://www.acmicpc.net/problem/6603
# DFS
def dfs(count, index):
    # 종료조건
    if count == 6:
        print(*lotto)
        return
    for i in range(index, k):
        lotto.append(array[i])
        dfs(count + 1, i + 1)
        lotto.pop()


while True:
    array = list(map(int, input().split()))
    k = array.pop(0)
    # 입력 종료 조건
    if k == 0:
        break
    # 로또번호 담을 배열
    lotto = []
    dfs(0, 0)
    print()


