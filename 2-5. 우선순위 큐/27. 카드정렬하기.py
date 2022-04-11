import heapq
import sys
input = sys.stdin.readline

# 카드를 힙에 넣기
n = int(input())
card = []
heapq.heapify(card)
for i in range(n):
    heapq.heappush(card, int(input()))

# 비교횟수
count = 0
while True:
    # 카드가 한그룹이면 비교할필요 없음
    if len(card) == 1:
        break

    # 힙에서 가장작은 두개 꺼내서 비교
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    c = a + b
    count = count + c

    # 힙이 빈경우 모두 합침
    if len(card) == 0:
        break
    heapq.heappush(card, c)

# 결과출력
print(count)