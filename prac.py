import sys
import bisect

M, N, L = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
x.sort()

ans = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if len(x) == 1:
        if abs(x[0] - a) + b <= L:
            ans += 1
    else:
        idx = bisect.bisect_left(x, a)
        print(a, idx)
        if idx == 0:
            if abs(x[idx] - a) + b <= L:
                ans += 1
        elif idx == len(x):
            if abs(x[idx - 1] - a) + b <= L:
                ans += 1
        else:
            if min(abs(x[idx - 1] - a), abs(x[idx] - a)) + b <= L:
                ans += 1
