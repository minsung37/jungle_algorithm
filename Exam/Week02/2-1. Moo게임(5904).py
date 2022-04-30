# https://www.acmicpc.net/problem/5904
n = int(input())

# n일때 문자열길이, 차수
length, k = 0, 0
while length < n:
    length = length + (k + 3) + length
    k = k + 1


def moo(length, center, n):
    # 이전차수 moo문자열 길이
    temp = (length - center) // 2

    # n이 center 기준 왼쪽에 있는 경우
    if n <= temp:
        moo(temp, center - 1, n)

    # n이 center 문자열에 있는 경우
    elif temp < n <= temp + center:
        if temp + 1 == n:
            print('m')
        else:
            print('o')

    # n이 center기준 오른쪽에 있는 경우
    elif temp + center < n:
        moo(temp, center - 1, n - temp - center)


# 정답 출력
moo(length, k + 2, n)