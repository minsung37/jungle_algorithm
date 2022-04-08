# 문제정보 입력받기
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

# 오름차순 정렬
array.sort()

# 정답출력
for i in range(n):
    print(array[i])