import itertools
import sys
input = sys.stdin.readline

# 난쟁이키 입력받기
array = []
for i in range(9):
    array.append(int(input()))
total = sum(array)

# 조합구하기
nCr = itertools.combinations(array, 7)
dwarf = list(nCr)

# 난쟁이 찾기
for i in dwarf:
    if sum(i) == 100:
        # 키순서로 출력
        i = list(i)
        i.sort()
        for j in i:
            print(j)
        break