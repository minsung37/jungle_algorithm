# 이해못함
while True:
    n, *temp = list(map(int, input().split()))
    if n == 0:
        break
    histogram = [0] + temp + [0]
    check = [0]
    area = 0

    for i in range(1, n + 2):
        while check and histogram[check[-1]] > histogram[i]:
            current = check.pop()
            print("current :", current)
            print("area :", area)
            print("histogram :", histogram)
            print("check :", check)
            area = max(area, (i - 1 - check[-1]) * histogram[current])
        check.append(i)
    print(area)