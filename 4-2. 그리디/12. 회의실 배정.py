import sys
input = sys.stdin.readline

# 시간 입력받아서 끝나는 시간 기준 정렬 => 시작시간기준 정렬
n = int(input())
schedule = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
# 종료시간과 회의개수 담을 변수
finish, count = 0, 0
# 가능한 회의 카운트
for start, end in schedule:
    if start >= finish:
        count = count + 1
        finish = end
# 정답 출력
print(count)