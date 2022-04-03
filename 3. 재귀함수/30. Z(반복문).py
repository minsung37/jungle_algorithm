# 문제조건 입력받기
n, r, c = map(int, input().split())
num = 0

# 순번 구하기
while n > 1:
    ran = 2 ** (n - 1)
    if r >= ran:
        # 4번째
        if c >= ran:
            num = num + (4 ** (n - 1)) * 3
            r = r - ran
            c = c - ran
        # 3번째
        else:
            num = num + (4 ** (n - 1)) * 2
            r = r - ran
    else:
        # 2번째
        if c >= ran:
            num = num + (4 ** (n - 1)) * 1
            c = c - ran
    n = n - 1

if r == 0:
    if c == 0:
        print(num)
    else:
        print(num + 1)
else:
    if c == 0:
        print(num + 2)
    else:
        print(num + 3)