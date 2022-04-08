from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(n):
    commend = input().split()

    # push X: 정수 X를 큐에 넣는 연산이다.
    if commend[0] == "push":
        queue.append(commend[1])

    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif commend[0] == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)

    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif commend[0] == "size":
        print(len(queue))

    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif commend[0] == "empty":
        if len(queue) > 0:
            print(0)
        else:
            print(1)

    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif commend[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif commend[0] == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)