import heapq
import sys
input = sys.stdin.readline

# 숫자개수 입력받기
n = int(input())

# 최대힙 최소힙
heap_max = []
heapq.heapify(heap_max)
heap_min = []
heapq.heapify(heap_min)

# 가운데를 말해요
for i in range(n):
    x = int(input())
    # 두 힙의 길이가 같은경우 최대힙에 넣어줌
    if len(heap_max) == len(heap_min):
        heapq.heappush(heap_max, -x)
    # 길이가 다른경우 최소힙에 넣어줌
    else:
        heapq.heappush(heap_min, x)
    # 최대힙의 최댓값 vs 최소힙의 최솟값 => 최대힙의 최댓값이 크면 둘을 바꿈
    if len(heap_max) >= 1 and len(heap_min) >= 1 and -(heap_max[0]) > heap_min[0]:
        a = -(heapq.heappop(heap_max))
        b = heapq.heappop(heap_min)
        heapq.heappush(heap_max, -b)
        heapq.heappush(heap_min, a)
    # 결과 출력
    print(-heap_max[0])