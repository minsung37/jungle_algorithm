import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    score = sorted([list(map(int, input().split())) for _ in range(n)])
    # 1차 1등의 2차 등수, 1차 1등은 선발
    compare, count = score[0][1], 1
    for i in range(1, n):
        # 1차 1등의 2차등수보다 높은등수 선발 => 탈락자 제외 1차 2(3,4...)등의 2차등수보다 높으면 선발
        if compare > score[i][1]:
            count = count + 1
            # 탈락자 제외 1차 2(3,4...)등의 2차 등수
            compare = score[i][1]
    print(count)