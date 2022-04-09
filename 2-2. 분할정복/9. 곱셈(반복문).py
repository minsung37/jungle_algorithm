import sys
input = sys.stdin.readline

# 문제 정보 입력받기
# (a ** b) % c
a, b, c = map(int, input().split())
array = []

while True:
    # 나뉘는수(a)가 큰 경우 먼저 나머지를 구함
    if a > c:
        a = a % c
    # 나누는수(c)가 큰 경우 나뉘는수(a) 제곱을함 => 곱해야하는수(b) 절반으로 줄어듦
    elif a < c:
        # 곱해야하는수(b)가 홀수인경우 현재 나뉘는수(a)를 array에 담음
        if b % 2 == 1:
            array.append(a % c)
        a = a ** 2
        b = b // 2
    # 나뉘는 수가 나누는수와 같아지면 나머지는 0이므로 반복문 탈출
    elif a == c:
        print(0)
        break
    # 곱해야하는수가 1이되면 반복문 탈출
    if b == 1:
        break

# 남은 요소와 a를 곱해준다.
for i in array:
    a = a * i

# 정답출력
print(a % c)