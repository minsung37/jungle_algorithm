import sys


class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        self.back = self.front = None

    def push(self, val):
        if self.front is None:
            self.back = self.front = LinkedList(val)
            self.size = 1
            return

        self.back.next = LinkedList(val)
        self.back = self.back.next
        self.size += 1
        return

    def pop(self):
        if self.front is None:
            return -1
        val = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.back = self.front
        self.size -= 1
        return val

    def empty(self):
        return 1 if self.size == 0 else 0


que = Queue()

N = int(sys.stdin.readline())
for _ in range(N):
    query = sys.stdin.readline().rstrip().split()
    if query[0] == "push":
        que.push(int(query[1]))

    elif query[0] == "pop":
        print(que.pop())

    elif query[0] == "size":
        print(que.size)

    elif query[0] == "empty":
        print(que.empty())

    elif query[0] == "front":
        if que.front is not None:
            print(que.front.val)
        else:
            print(-1)

    elif query[0] == "back":
        if que.back is not None:
            print(que.back.val)
        else:
            print(-1)