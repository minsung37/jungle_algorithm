import heapq
import sys
input = sys.stdin.readline
limit = 100000

# 도시, 노선 개수
n = int(input())
m = int(input())

# 연결리스트, 방문체크, 최단거리 테이블
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [limit] * (n + 1)

# 노선정보 (a에서 b로 가는 비용이 c다)
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
start, end = map(int, input().split())


def dijkstra(start):
    queue = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        min_dist, now = heapq.heappop(queue)
        # 현재 노드가 이미 저리된 적이 있는 노드라면 무시
        if distance[now] < min_dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = min_dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)
# 정답출력
print(distance[end])