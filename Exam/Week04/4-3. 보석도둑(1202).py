# https://www.acmicpc.net/problem/1202(보석도둑)
import sys
input = sys.stdin.readline

# 보석은 가격기준 내림차순, 가방은 오름차순
n, k = map(int, input().split())
stones = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1], reverse=True)
bags = sorted([int(input()) for _ in range(k)])

# 비싸고 가벼운거 먼저챙기기
count = 0
for stone in stones:
    if not bags:
        break
    weight = stone[0]
    value = stone[1]
    for bag in bags:
        if weight <= bag:
            count = count + value
            bags.remove(bag)
            break
print(count)
