# 테스트케이스 수
n = int(input())

# O만 더하기
for i in range(n):
    total_score = 0
    score = 1
    quiz = input()
    for j in quiz:
        if j == "O":
            total_score = total_score + score
            score = score + 1
        else:
            score = 1
    print(total_score)