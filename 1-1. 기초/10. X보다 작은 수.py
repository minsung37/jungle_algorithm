# 문제조건 입력받기
n, x = map(int, input().split())
array = list(map(int, input().split()))

# x 보다 작은수 출력
for i in range(n):
    if array[i] < x:
        print(array[i], end=" ")