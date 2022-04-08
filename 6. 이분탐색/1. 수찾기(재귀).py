# sample안의 수가 array안에 존재하는는지 확인
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
sample = list(map(int, input().split()))


# 이진탐색(재귀)
def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


# 정답 출력
for i in sample:
    print(binary_search(array, i, 0, n - 1))