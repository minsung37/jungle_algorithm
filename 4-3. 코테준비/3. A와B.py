import sys
input = sys.stdin.readline

# 단어 2개 입력받기
s = list(map(str, input().rstrip()))
t = list(map(str, input().rstrip()))

for _ in range(len(t) - len(s)):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
if s == t:
    print(1)
else:
    print(0)