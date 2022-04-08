def dfs(count):
    # 수열 n개를 모두 고르면
    if count == n:
        result.append(sum(abs(sequence[i] - sequence[i + 1]) for i in range(n - 1)))
        return
    for i in range(n):
        # 수를 사용한경우
        if visited[i]:
            continue
        sequence.append(array[i])
        visited[i] = True
        dfs(count + 1)
        visited[i] = False
        sequence.pop()


# 문제정보 입력받기
n = int(input())
array = list(map(int, input().split()))
# 결과, 수열을 담을 변수
result, sequence = [], []
# 방문목록
visited = [False] * n
# 탐색시작
dfs(0)
print(max(result))