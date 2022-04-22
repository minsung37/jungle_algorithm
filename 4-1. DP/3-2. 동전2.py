n, k = map(int, input().split())

# 코인입력받고 정렬
coin = sorted([int(input()) for _ in range(n)])

# dp 테이블 만들기
dp = [10001] * (k + 1)
dp[0] = 0

# 최소 개수 구하기
for i in coin:
    for j in range(i, k + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)

# 정답 출력
if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])


# 1원은 0원에 1원을 더하는 방법으로 만들 수 있다. 1번
# 2원은 1원에 1원을 더하는 방법으로 만들 수 있다. 2번
# ...
# 5원은 0원에 5원을 더하는 방법으로 만들 수 있다. 1번
# 6원은 1원에 5원을 더하는 방법으로 만들 수 있다. 2번