# https://www.acmicpc.net/problem/16120
import sys
input = sys.stdin.readline

word = list(input().rstrip())
stack = []

# PPAP 문자열 검사
for i in word:
    stack.append(i)
    # 스택에서 꺼낸 최근 4개가 PPAP이면 PAP를 뺸다.
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            stack.pop()


if stack == ['P']:
    print('PPAP')
else:
    print('NP')