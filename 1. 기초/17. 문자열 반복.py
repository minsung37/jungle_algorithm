# 테스트케이스의 개수
t = int(input())
for i in range(t):
    # 반복횟수, 반복문자열
    r, s = map(str, input().split())
    for j in s:
        print(j * int(r), end="")
    print()