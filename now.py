import sys
input = sys.stdin.readline

# M: 사대의수, N: 동물의수, L: 사정거리
M, N, L = map(int, input().split())
spot = sorted(list(map(int, input().split())))
animal = []
for i in range(N):
    temp = list(map(int, input().split()))
    if temp[1] <= L:
        animal.append(temp)

hunt = 0
for a, b in animal:
    start, end = 0, M - 1
    while start < end:
        mid = (start + end) // 2
        if spot[mid] < a:
            start = mid + 1
        elif spot[mid] > a:
            end = mid - 1
        else:
            start = mid
            break
    if abs(spot[start] - a) + b <= L:
        hunt = hunt + 1
    # 오른쪽 사대
    elif start + 1 < len(spot) and abs(spot[start + 1] - a) + b <= L:
        hunt = hunt + 1
    # 왼쪽 사대
    elif start > 0 and abs(spot[start - 1] - a) + b <= L:
        hunt = hunt + 1
print(hunt)