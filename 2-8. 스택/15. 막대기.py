import sys
input = sys.stdin.readline

# 막대기정보 입력받기
n = int(input())
stack = [int(input()) for _ in range(n)]

k = -1
count = 0
while stack:
    if stack[-1] > k:
        k = stack[-1]
        count = count + 1
    stack.pop()
print(count)
