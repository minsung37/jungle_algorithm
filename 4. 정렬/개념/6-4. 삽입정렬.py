# 정렬할 배열
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

flag, count = 0, 0
print(flag, "번째 :", *array)

# 삽입정렬 : 시간복잡도 O(N^2), 최선의 경우 O(N) => 어느정도 정렬이 되어있는 경우
for i in range(1, len(array)):
    # 인덱스 i부터 1까지 감소하며 반복하는 문법
    for j in range(i, 0, -1):
        count = count + 1
        # 한칸씩 왼쪽으로 이동
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            flag = flag + 1
            print(flag, "번째 :", *array)
        else:
            print("---")
            break
print("연산횟수 :", count)
