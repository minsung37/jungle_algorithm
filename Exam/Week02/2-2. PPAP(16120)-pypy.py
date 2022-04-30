# https://www.acmicpc.net/problem/16120
import sys
input = sys.stdin.readline

word = input().rstrip()
ppap = 'PPAP'
n = len(word)

# 문자열 담을 스택
stack = []
for i in range(n):
    stack.append(word[i])
    if stack[-1] == ppap[-1] and len(stack) >= 4:
        count = 1
        for j in range(1, 4):
            if stack[- 1 - j] == ppap[- 1 - j]:
                count = count + 1
        # PPAP가 있는경우 P로 치환
        if count == 4:
            for _ in range(3):
                stack.pop()

# 정답출력
if stack == ['P']:
    print("PPAP")
else:
    print("NP")
