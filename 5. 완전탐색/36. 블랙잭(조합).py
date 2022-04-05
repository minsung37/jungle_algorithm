import itertools
import sys
input = sys.stdin.readline

# 문제정보 입력받기
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 3개 조합 구하기
nCr = itertools.combinations(numbers, 3)
blackjack = list(nCr)

# 블랙잭 조합의 합을 담을 리스트
blackjack_sum = []
for i in blackjack:
    x = sum(i)
    # 수의 합이 m 보다 작거나 같은것만 리스트에 담기
    if m - x >= 0:
        blackjack_sum.append(x)

# 최대값 출력
print(max(blackjack_sum))
