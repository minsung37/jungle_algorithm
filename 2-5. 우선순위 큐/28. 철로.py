import heapq
import sys
input = sys.stdin.readline

# 문제조건 입력받기
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
d = int(input())

# array중 거리가 d이하인것만 정렬해서 담기
road = []
for i in array:
    if abs(i[0] - i[1]) <= d:
        temp = [i[0], i[1]]
        road.append(sorted(temp))
road.sort(key=lambda x: x[1])

# 최대값 담을변수
result, heap = 0, []
heapq.heapify(heap)

for i in road:
    if not heap:
        heapq.heappush(heap, i)
    else:
        # 선분에 포함이 안되는 경우 반복해서 힙에서 제거하기
        while heap[0][0] < i[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, i)
    result = max(result, len(heap))
print(result)
# 끝점 - 선분길이 > 시작점 인경우 힙에서 빼기