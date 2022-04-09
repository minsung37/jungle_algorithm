import sys


class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.size = 0
        self.last = None

    def push(self, val):
        self.last = LinkedList(val, self.last)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1

        self.size -= 1
        val = self.last.val
        self.last = self.last.next
        return val

    def empty(self):
        return 1 if self.size == 0 else 0

    def top(self):
        if self.last is None:
            return -1
        return self.last.val


N = int(sys.stdin.readline())

stack = Stack()
for _ in range(N):
    query = sys.stdin.readline().split()
    if query[0] == "push":
        val = int(query[1])
        stack.push(val)
    elif query[0] == "pop":
        print(stack.pop())
    elif query[0] == "size":
        print(stack.size)
    elif query[0] == "empty":
        print(stack.empty())
    elif query[0] == "top":
        print(stack.top())