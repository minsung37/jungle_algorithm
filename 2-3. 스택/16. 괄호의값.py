import sys
input = sys.stdin.readline
ps = list(input().rstrip())
stack, result, temp, n = [], 0, 1, len(ps)

# 괄호열 계산
for i in range(n):
    if ps[i] == "(":
        temp = temp * 2
        stack.append(ps[i])
    elif ps[i] == "[":
        temp = temp * 3
        stack.append(ps[i])
    elif ps[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if ps[i - 1] == "(":
            result = result + temp
        stack.pop()
        temp = temp // 2
    else:  # "]"인 경우
        if not stack or stack[-1] == "(":
            result = 0
            break
        if ps[i - 1] == "[":
            result = result + temp
        stack.pop()
        temp = temp // 3
# 결과출력
if stack:
    print(0)
else:
    print(result)
