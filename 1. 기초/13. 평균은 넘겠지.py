# 테스트케이스의 수
c = int(input())
for i in range(c):
    # 평균넘는학생 수
    count = 0
    # 학생들 정보
    score = list(map(int, input().split()))
    n = score[0]
    score.pop(0)
    avg = sum(score) / n
    for k in score:
        if k > avg:
            count = count + 1
    rate = count / n * 100
    print(f'{rate:.3f}%')