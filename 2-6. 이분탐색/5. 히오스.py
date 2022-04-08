n, k = map(int, input().split())
level = sorted([int(input()) for _ in range(n)])
# 끝값 설정
start = min(level)
end = max(level) + k

# 이분 탐색
res = 0
while start <= end:
    mid = (start + end) // 2
    # mid까지 올린 캐릭터의 레벨합
    temp = 0
    for i in level:
        if i >= mid:
            break
        temp = temp + (mid - i)
    # 레벨 더 올려야함 => 뒤쪽 탐색
    if temp <= k:
        res = mid
        start = mid + 1
    # 앞쪽 탐색
    else:
        end = mid - 1
print(res)
