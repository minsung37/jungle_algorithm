x, y, w, h = map(int, input().split())
# 가로까지거리, 세로까지거리, 축까지의 거리(2개) 중 최소값 출력
print(min(h - y, w - x, x, y))
