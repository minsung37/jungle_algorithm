# 정렬할 배열
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

flag, count = 0, 0
print(0, "번째 :", *array)


# 퀵정렬 : 시간복잡도 평균적으로 O(NlogN)
def quick_sort(array, start, end):
    global flag, count
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left = left + 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right = right - 1
        # 엇갈렸다면 작은 right = right - 1 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        flag = flag + 1
        count = count + 1
        print(flag, "번째 :", *array)
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
print("연산횟수 :", count)