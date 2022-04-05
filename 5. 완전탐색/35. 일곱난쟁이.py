import sys
input = sys.stdin.readline

# 난쟁이키 입력받기
array = []
for i in range(9):
    array.append(int(input()))
total = sum(array)

# 제외할 난쟁이 구하기
x, y = 0, 0
for i in array:
    for j in array:
        if i != j:
            if total - (i + j) == 100:
                x, y = i, j

# 난쟁이 제외하기
array.remove(x)
array.remove(y)

# 키순으로 출력
array.sort()
for i in array:
    print(i)