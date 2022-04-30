# https://www.acmicpc.net/problem/1924
x, y = map(int, input().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, x):
    y = y + day_per_month[i]

# 정답출력
print(day[y % 7])