# cards n개 중에 k개 뽑기
n = int(input())
k = int(input())
cards = list(input() for i in range(n))
# set사용 중복제거
result = set()


def makenum(count, permutation, visited):
    # k장 뽑으면 합치기
    if count == k:
        result.add(''.join(permutation))
        return
    for i in range(n):
        # 방문한적 없으면
        if not visited[i]:
            visited[i] = True
            makenum(count + 1, permutation + [cards[i]], visited)
            visited[i] = False


makenum(0, [], [False] * n)
print(len(result))