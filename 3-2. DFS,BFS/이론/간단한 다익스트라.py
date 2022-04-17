import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c다
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallist_node():
    min_value = INF
    # 가장 최단 거리가 짧은 노드
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
