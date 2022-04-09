from typing import Any


class Stack:
    # 비어 있는 Fixedstack에 팝 또는 피크할 때 내보내는 예외처리
    class Empty(Exception):
        pass

    # 가득찬 FixedStack에 푸시할 때 내보내는 예외처리
    class Full(Exception):
        pass

    # 스택초기화
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity  # 스택의 크기
        self.ptr = 0  # 스택 포인터

    # 스택이 가득 차 있는지 판단
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    # 스택에 value를 푸시(데이터를 넣음)
    def push(self, value: Any) -> None:
        if self.is_full():  # 스택이 가득 차 있는 경우
            raise Stack.Full  # 예외처리 발생
        self.stk[self.ptr] = value
        self.ptr = self.ptr + 1

    # 스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)
    def pop(self) -> Any:
        if self.empty():  # 스택이 비어 있음
            raise Stack.Empty  # 예외처리 발생
        self.ptr = self.ptr - 1
        return self.stk[self.ptr]

    def size(self) -> int:
        return self.ptr

    # 스택이 비어 있는지 판단
    def empty(self) -> bool:
        if self.ptr <= 0:
            return 1
        else:
            return 0

    # 스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)
    def top(self) -> Any:
        if self.empty():  # 스택이 비어 있음
            return -1
        else:
            return self.stk[self.ptr - 1]


n = int(input())
stack = Stack()
for _ in range(n):
    commend = input().split()
    if commend[0] == "push":
        stack.push(int(commend[1]))
    elif commend[0] == "pop":
        print(stack.pop())
    elif commend[0] == "size":
        print(stack.size)
    elif commend[0] == "empty":
        print(stack.empty())
    elif commend[0] == "top":
        print(stack.top())