# n 나무수, m 목표나무길이, tree 각각나무길이
n, m = map(int, input().split())
tree = list(map(int, input().split()))
# 이진 탐색 시작값, 끝값
start = 0
end = max(tree)


# 나무자르기 함수
def cut(mid):
    res = 0
    for i in tree:
        if i > mid:
            res = res + i - mid
    return res


# 이진탐색
result = 0
while start < end:
    mid = (start + end) // 2
    total = cut(mid)
    if m <= total:
        result = mid
        start = mid + 1
    else:
        end = mid
print(result)
