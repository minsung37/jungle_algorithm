import sys
input = sys.stdin.readline

# 계수정렬 => 수의범위만큼 배열 만들기
n = int(input())
limit = 10001
counting_sort = [0] * 10001

# 입력받은 값 => 인덱스 => 1증가
for i in range(n):
    a = int(input())
    counting_sort[a] = counting_sort[a] + 1

# i를 counting_sort[i]번 출력
for i in range(len(counting_sort)):
    for j in range(counting_sort[i]):
        print(i)