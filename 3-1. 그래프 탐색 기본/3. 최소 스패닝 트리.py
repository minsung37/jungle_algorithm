# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 부모 배치
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은애를 부모로 만들기
    if a < b:
        # b의 부모는 a
        parent[b] = a
        # a의 부모는 b
    else:
        parent[a] = b


# 정점과 간선의 개수 입력받기
v, e = map(int, input().split())

# 간선정보를 입력받아 비용순 정렬
edges, result = [], 0
for _ in range(v):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

# 부모를 자기 자신으로 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# 간선을 하나씩 확인하면서
for edge in edges:
    cost, a, b = edge
    # 서로 연결된 요소의 부모가 같은 경우에 사이클이 형성된다.(사이클이 형성되지 않아야함)
    if find_parent(parent, a) != find_parent(parent, b):
        # a, b 부모관계 만들어줌(작은애가 부모)
        union_parent(parent, a, b)
        # 결과 계산
        result = result + cost
print(result)