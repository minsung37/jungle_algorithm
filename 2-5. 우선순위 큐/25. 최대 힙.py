import heapq
import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

# 리스트를 힙으로
heap = []
heapq.heapify(heap)
for i in array:
    # 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우
    if i == 0 and len(heap) == 0:
        print(0)
    # 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
    elif i == 0:
        print(abs(heapq.heappop(heap)))
    # 힙에 원소 넣기
    else:
        heapq.heappush(heap, -i)
