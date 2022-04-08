import sys
input = sys.stdin.readline

# n개의 집에 c개의 공유기 설치
n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()

# 공유기 간격의 최소값, 최대값
mn = 1
mx = array[-1] - array[0]

# 인접한공유기 사이의 최대 거리
result = 0

# 이분탐색
while mn <= mx:
    mid = (mx + mn) // 2
    # 초기 공유기 설치 위치
    spot = array[0]
    count = 1
    for i in range(1, n):
        # 공유기 설치하기
        if array[i] >= spot + mid:
            spot = array[i]
            count = count + 1
    # 더 설치 해야함 => 간격 좁히기
    if count < c:
        mx = mid - 1
    # 목표개수 오바한경우 => 간격 줄여야함
    else:
        mn = mid + 1
        result = mid
# 정답출력
print(result)