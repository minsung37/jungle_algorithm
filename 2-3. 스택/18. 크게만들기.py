import sys
input = sys.stdin.readline

# n자리의 수에서 k개를 지워서 가장크게 만들기
n, k = map(int, input().split())
number = list(input().rstrip())
stack, count = [], 0

# 지우기
for i in range(n):
    # 숫자를 지울수 있고, 스택이 비어있지 않고, 뒷자리 수 보다 작을때
    while count < k and stack and stack[-1] < number[i]:
        stack.pop()
        count = count + 1
    stack.append(number[i])

# 정답출력(여기서 k를 사용하기 때문에 count에 할당해야함)
print(''.join(stack[:n - k]))