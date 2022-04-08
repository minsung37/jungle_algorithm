import sys
input = sys.stdin.readline
n = int(input())

# VPS 검사
for i in range(n):
    ps = input().rstrip()
    count = 0
    for j in ps:
        if j == "(":
            count = count + 1
        else:
            count = count - 1
        # ")"가 먼저나온 경우는 VPS가 될 수 없다.
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")