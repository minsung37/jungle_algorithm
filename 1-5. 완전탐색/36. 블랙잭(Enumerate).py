import sys
input = sys.stdin.readline

# 문제 정보 입력받고 카드 정렬
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

# 블랙잭 결과를 담을 변수
blackjack_sum = []

for i, num in enumerate(numbers):
    if num > m:
        break
    acc = num
    for j in range(i + 1, len(numbers)):
        j_val = numbers[j]
        if acc + j_val > m:
            break
        second_acc = acc + j_val
        for k in range(j + 1, len(numbers)):
            k_val = numbers[k]
            if acc + k_val > m:
                break
            last_acc = second_acc + k_val
            if last_acc <= m:
                blackjack_sum.append(last_acc)

# 정답출력
print(max(blackjack_sum))