# 정렬할 배열
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

flag, count = 0, 0
print(flag, "번째 :", *array)

# 선택정렬 : 시간복잡도 O(N^2)
for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i
    for j in range(i + 1, len(array)):
        count = count + 1
        if array[min_index] > array[j]:
            min_index = j
    # 스와프
    array[i], array[min_index] = array[min_index], array[i]
    flag = flag + 1
    print(flag, "번째 :", *array)
print("연산횟수 :", count)
