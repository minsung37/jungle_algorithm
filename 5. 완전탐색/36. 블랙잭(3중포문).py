import sys
input = sys.stdin.readline

# 문제정보 입력받기
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 3개 조합 더하기
blackjack = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                value = numbers[i] + numbers[j] + numbers[k]
                if value <= m:
                    blackjack.append(value)

# 최대값 출력
print(max(blackjack))
