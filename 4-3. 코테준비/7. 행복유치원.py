import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = list(map(int, input().split()))

# 인접한 학생수간 차이를 담고 정렬
temp = []
for i in range(1, n):
    x = students[i] - students[i - 1]
    temp.append(x)
temp.sort()

# 결과출력
print(sum(temp[:n - k]))