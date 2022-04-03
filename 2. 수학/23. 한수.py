# n보다 작은 한수 구하기 (n < 1000)
n = int(input())
# 한자리, 두자리수는 모두 한수
if n < 100:
    print(n)
# 3자리 수중 한수 구하기
else:
    # 세자리수 중에 한수
    count = 0
    for i in range(100, n + 1):
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            count = count + 1
    print(99 + count)