# 시간 복잡도 더 낮음
n, k = map(int, input().split())
array = []
for i in range(n):
    array.append(i + 1)

# 요세푸스 수열 구하기
josephus = []
order = k - 1
for i in range(n):
    order = order % n
    josephus_number = array.pop(order)
    josephus.append(str(josephus_number))
    order = order + (k - 1)
    # 한명 빠져나감
    n = n - 1

# 정답 출력
print("<" + ", ".join(josephus) + ">")