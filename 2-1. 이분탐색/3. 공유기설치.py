import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = sorted([int(input()) for _ in range(n)])

start = -1
end = 10**9+1

while start < end:
    mid = (end + start) // 2
    spot = array[0]
    count = 1
    for i in range(1, n):
        if array[i] >= spot + mid:
            spot = array[i]
            count = count + 1
    if c <= count:
        start = mid + 1
    else:
        end = mid
# 정답출력
print(start - 1)