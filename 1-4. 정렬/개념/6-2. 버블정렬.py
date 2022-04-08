# 정렬할 배열
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

flag, count = 0, 0
print(0, "번째 :", *array)

# 버블정렬 : 시간복잡도 O(N^2)
n = len(array)
for i in range(n):
    # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
    for j in range(0, n - i - 1):
        count = count + 1
        # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]  # 서로 위치를 변환
            flag = flag + 1
            print(flag, "번째 :", *array)
print("연산횟수 :", count)




