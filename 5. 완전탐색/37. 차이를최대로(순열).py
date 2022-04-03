import itertools
import sys
input = sys.stdin.readline

# 문제조건 입력받기
n = int(input())
numbers = list(map(int, input().split()))

# 모든 경우
nPr = itertools.permutations(numbers, n)
all_case = list(nPr)

# 모든 경우의 합을 구해서 배열에 넣기
sum_all_case = []
for i in all_case:
    result = 0
    for j in range(1, n):
        temp = abs(i[j] - i[j - 1])
        result = result + temp
    sum_all_case.append(result)

# 최대값 출력
print(max(sum_all_case))
