# 문제입력받기
array = []
for i in range(9):
    array.append(int(input()))

# 최대값
mx = max(array)

# 정답출력
print(mx)
print(array.index(mx) + 1)