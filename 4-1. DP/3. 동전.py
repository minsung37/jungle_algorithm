import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1
    # target원의 가지수를 구하려면 target - i 원을 만드는 가지수를 구해야한다.
    for i in coin:
        for j in range(1, target + 1):
            if j >= i:
                dp[j] = dp[j] + dp[j - i]
    # 정답출력
    print(dp[-1])