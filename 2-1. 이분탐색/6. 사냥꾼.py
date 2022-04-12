import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
spot = sorted(list(map(int, input().split())))
animal = []
for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[1] <= L:
        animal.append(temp)

# 사냥한 동물수
hunt = 0
for a, b in animal:
    start, end = 0, M - 1
    # bisect_left
    while start < end:
        mid = (start + end) // 2
        if spot[mid] < a:
            start = mid + 1
        else:
            end = mid
    if len(spot) == 1:
        if abs(spot[0] - a) + b <= L:
            hunt = hunt + 1
    else:
        # 시작점
        if start == 0:
            if abs(spot[start] - a) + b <= L:
                hunt = hunt + 1
        # 오른쪽 끝 사대 보다 옆에 있는 경우
        elif start == len(spot):
            if abs(spot[start - 1] - a) + b <= L:
                hunt = hunt + 1
        # 사이
        else:
            if min(abs(spot[start - 1] - a), abs(spot[start] - a)) + b <= L:
                hunt = hunt + 1
print(hunt)