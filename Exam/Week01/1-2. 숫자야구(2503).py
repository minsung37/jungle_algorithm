# https://www.acmicpc.net/problem/2503
# 범위 : 123 ~ 987
array = [True] * 1000
for i in range(123, 988):
    str_i = str(i)
    # 0들어간수 제외
    if "0" in str_i:
        array[i] = False
    # 중복된 숫자 들어간수 제외
    if len(set(str_i)) < 3:
        array[i] = False

# 숫자야구시작
n = int(input())
for _ in range(n):
    number, s, b = map(int, input().split())
    # 상대가 부른 숫자
    check_num = str(number)
    for i in range(123, 988):
        # 내가 생각하는 숫자
        think_num = str(i)
        # strike, ball 초기화
        strike, ball = 0, 0
        for x in range(3):
            for y in range(3):
                # 같은숫자가 있을때
                if check_num[x] == think_num[y]:
                    # 인덱스값이 같으면 strike
                    if x == y:
                        strike = strike + 1
                    # 인덱스값이 다르면 ball
                    else:
                        ball = ball + 1
        if strike != s or ball != b:
            array[i] = False

# 정답출력
count = 0
for i in range(123, 988):
    if array[i]:
        count = count + 1
print(count)
