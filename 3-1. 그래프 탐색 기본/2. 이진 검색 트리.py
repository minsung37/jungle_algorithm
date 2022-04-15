import sys
sys.setrecursionlimit(10 ** 6)

# 입력받은수 배열에 담기
numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break


# 후위 순회
def postorder(first, end):

    if first > end:
        return
    mid = end + 1  # 루트보다 큰 값이 존재하지 않을 경우를 대비
    for i in range(first + 1, end + 1):
        if numbers[first] < numbers[i]:
            mid = i
            break

    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(numbers[first])


postorder(0, len(numbers) - 1)