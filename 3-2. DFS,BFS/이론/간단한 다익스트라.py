import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수, 시작노드 번호
n, m = map(int, input().split())
start = int(input())

# 연결리스트, 방문체크, 최단거리 테이블
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 모든 간선정보를 입력받기(a에서 b로 가는 비용이 c다)
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def get_smallist_node():
    min_value = INF
    # 가장 최단 거리가 짧은 노드
    index = 0
    for i in range(1, n + 1):
        # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        # b로 가는 비용 바꾸기
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallist_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]
# 0    1                         2                 3                 4                 5                  6
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2