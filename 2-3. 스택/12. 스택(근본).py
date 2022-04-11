from typing import Any
import sys
input = sys.stdin.readline


class Stack:
    # 스택초기화
    def __init__(self, capacity: int = 99999) -> None:
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity  # 스택의 크기
        self.ptr = 0  # 스택 포인터
        pass

    # 스택이 가득 차 있는지 판단
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    # 스택에 value를 푸시(데이터를 넣음)
    def push(self, value: Any) -> None:
        self.stk[self.ptr] = value
        self.ptr = self.ptr + 1

    # 스택이 비어 있는지 판단
    def is_empty(self) -> bool:
        if self.ptr <= 0:
            return 1
        return 0

    # 스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)
    def pop(self) -> int:
        if self.is_empty():  # 스택이 비어 있음
            return -1  # 예외처리 발생
        self.ptr = self.ptr - 1
        return self.stk[self.ptr]

    # 스택의 길이 확인
    def size(self) -> int:
        return self.ptr

    # 스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)
    def top(self) -> Any:
        if self.is_empty():  # 스택이 비어 있음
            return -1
        return self.stk[self.ptr - 1]


n = int(input())
stack = Stack()
for _ in range(n):
    commend, *v = input().split()
    if commend == "push":
        stack.push(int(v[0]))
    elif commend == "pop":
        print(stack.pop())
    elif commend == "size":
        print(stack.size())
    elif commend == "empty":
        print(stack.is_empty())
    elif commend == "top":
        print(stack.top())
