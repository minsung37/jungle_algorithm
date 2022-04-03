# 퀸을 놓는 함수
def queen(chess, n, x):
    count = 0
    if n == x:
        return 1
    for y in range(n):
        # (x, y)에 퀸을 놓음
        chess[x] = y
        for k in range(x):
            # 세로로 겹치는 경우 세지않는다.
            if chess[x] == chess[k]:
                break
            # 대각으로 겹치는 경우 세지않음
            if abs(chess[x] - chess[k]) == abs(x - k):
                break
        # for 문이 모두 실행된 경우에 실행됨
        else:
            count = count + queen(chess, n, x + 1)
    return count


# 정답출력
n = int(input())
chess = [0] * n
print(queen(chess, n, 0))