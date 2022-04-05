# 문제조건 입력받기
a, b, v = map(int, input().split())

# 낮밤동안 올라가는 높이
climbing = a - b
day = 0

# 마지막날 a만큼 올라가면 알맞게 정상도달
if (v - a) % climbing == 0:
    day = (v - a) // climbing + 1

# 마지막날 a만큼 올라가도 정상에 도달 못한 경우 다음날 한번 더 올라야함
else:
    day = (v - a) // climbing + 2

# 정답출력
print(day)