import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    commend = int(input())
    # 방금 부른수 빼기
    if commend == 0:
        stack.pop()
    # 스택에 넣기
    else:
        stack.append(commend)
# 결과출력
print(sum(stack))