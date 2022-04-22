import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 동전 입력 받고 역순 정렬
coin = sorted([int(input()) for _ in range(n)], reverse=True)
# 동전개수
count = 0
# 동전 카운트
for i in range(n):
    # 큰 금액으로 나누어 떨어지는 경우
    if k % coin[i] < k:
        count = count + k // coin[i]
        # 남은금액
        k = k % coin[i]
# 정답출력
print(count)