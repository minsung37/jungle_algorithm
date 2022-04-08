from collections import deque

n, k = map(int, input().split())
queue = deque()
for i in range(n):
    queue.append(i + 1)

# 요세푸스 수열 만들기
josephus = []
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    josephus.append(queue.popleft())

# 정답 출력
print("<", end='')
for i in range(n - 1):
    print("%d, " % josephus[i], end='')
print(josephus[-1], end='')
print(">")
