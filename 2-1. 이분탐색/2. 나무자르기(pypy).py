# n 나무수, m 목표나무길이, tree 각각나무길이
n, m = map(int, input().split())
tree = list(map(int, input().split()))
# 이진 탐색 시작값, 끝값
start = 0
end = max(tree)
# 잘린 나무 길이의 합
result = 0

while start <= end:
    mid = (start + end) // 2
    # 나무자르기
    res = 0
    for i in tree:
        if i > mid:
            res = res + i - mid
    if res < m:
        end = mid - 1
    else:
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1
        result = mid
# 결과출력
print(result)

# 파이썬 시간초과, pypy3 정답