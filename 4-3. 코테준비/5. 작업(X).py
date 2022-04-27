import sys
workut = sys.stdin.readline

n = int(workut())
dp = [0]
for i in range(n):
    work = list(map(int, input().split()))
    time, pre_work_num, pre_work = work[0], work[1], work[2:]
    dp.append(time + dp[max(pre_work, key=lambda x: dp[x], default=0)])
print(max(dp))
print(dp)