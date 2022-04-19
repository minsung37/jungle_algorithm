import sys
input = sys.stdin.readline

# 가벼운거 탐색, 무거운거 탐색
n, m = map(int, input().split())
light = [[] for _ in range(n + 1)]
heavy = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    light[a].append(b)
    heavy[b].append(a)
# 중간위치
mid = (n + 1) // 2


# 가벼운거 찾기
def dfs_find_light(v):
    global count_light
    light_visited[v] = True
    for i in light[v]:
        # 방문한적 없으면
        if not light_visited[i]:
            dfs_find_light(i)
            count_light = count_light + 1
    return count_light


# 무거운거 찾기
def dfs_find_heavy(v):
    global count_heavy
    heavy_visited[v] = True
    for i in heavy[v]:
        # 방문한적 없으면
        if not heavy_visited[i]:
            dfs_find_heavy(i)
            count_heavy = count_heavy + 1
    return count_heavy


# 중간이 될 수 없는 구슬 개수
result = 0
for i in range(1, n + 1):
    count_light, count_heavy = 0, 0
    light_visited = [False] * (n + 1)
    heavy_visited = [False] * (n + 1)
    x = dfs_find_light(i)
    y = dfs_find_heavy(i)
    if x >= mid or y >= mid:
        result = result + 1
print(result)