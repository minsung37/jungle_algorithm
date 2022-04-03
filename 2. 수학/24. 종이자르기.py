# 종이의 가로, 세로의 길이 입력받기
x, y = map(int, input().split())
n = int(input())

# 자를 종이의 길이 입력 받기
width = [x]
height = [y]
for i in range(n):
    a, b = map(int, input().split())
    if a == 1:
        width.append(b)
    else:
        height.append(b)

# 작은거부터 자르기
width.sort()
height.sort()

# 0 ~ 가장 작은값 자른 길이
cut_width = [width[0]]
cut_height = [height[0]]

# 자른 종이의 길이 배열에 담기
for i in range(1, len(width)):
    cut_width.append(width[i] - width[i - 1])
for i in range(1, len(height)):
    cut_height.append(height[i] - height[i - 1])

# 정답 출력
print(max(cut_width) * max(cut_height))