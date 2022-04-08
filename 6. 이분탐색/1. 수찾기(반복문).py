# sample안의 수가 array안에 존재하는는지 확인
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
sample = list(map(int, input().split()))


# 이진탐색(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 수가 존재하는 경우
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    # 수가 존재하지 않는 경우
    return 0


# 정답 출력
for i in sample:
    print(binary_search(array, i, 0, n - 1))