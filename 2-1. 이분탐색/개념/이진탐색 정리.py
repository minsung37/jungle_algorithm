array = [1, 1, 2, 4, 5, 5, 6, 8, 9, 9, 11, 15]
#        0  1  2  3  4  5  6  7  8  9  10  11
start = 0
end = len(array) - 1

# n을 어디에 추가할래

# bisect_left - 왼쪽기준으로 추가
n = 3
while start < end:
    mid = (start + end) // 2
    if array[mid] < n:
        start = mid + 1
    else:
        end = mid
print("(bisect_left)", n, "의위치 :", start)

# bisect_right - 오른쪽기준으로 추가
start = 0
end = len(array) - 1
while start < end:
    mid = (start + end) // 2
    if array[mid] <= n:
        start = mid + 1
    else:
        end = mid
print("(bisect_right)", n, "의위치 :", start)