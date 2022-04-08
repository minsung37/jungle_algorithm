# 문제조건 입력받기
n = int(input())
array = list(map(int, input().split()))
result = 0

# 소수의 개수 구하기
for i in array:
    # 약수의 개수
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    # 약수의 개수가 2개이면 소수이다.
    if count == 2:
        result = result + 1

# 정답출력
print(result)