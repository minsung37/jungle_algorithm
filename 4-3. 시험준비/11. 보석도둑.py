import sys
import heapq
input = sys.stdin.readline

# 보석은 비싼거부터, 가방은 가벼운거부터
n, k = map(int, input().split())
stones, bags = [], []
for _ in range(n):
    heapq.heappush(stones, list(map(int, input().split())))
for _ in range(k):
    bags.append(int(input()))
bags.sort()

# 비싼거 가벼운가방에 먼저챙기기
value, temp = 0, []
for bag in bags:
    # 보석이 있고 가방에 들어갈때 힙에넣기
    while stones and bag >= stones[0][0]:
        heapq.heappush(temp, -heapq.heappop(stones)[1])
    if temp:
        # 비싼거 챙기기
        value = value - heapq.heappop(temp)
    elif not stones:
        break
print(value)
