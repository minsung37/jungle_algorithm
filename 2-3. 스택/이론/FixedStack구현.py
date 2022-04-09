# 고정 길이 스택 클래스 FixedStack 구현하기
from typing import Any


# 고정 길이 스택 클래스
class FixedStack:
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

    # 스택에 쌓여있는 데이터 개수를 반환
    def __len__(self) -> int:
        return self.ptr

    # 스택이 비어 있는지 판단
    def is_empty(self) -> bool:
        return self.ptr <= 0

    # 스택이 가득 차 있는지 판단
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    # 스택에 value를 푸시(데이터를 넣음)
    def push(self, value: Any) -> None:
        if self.is_full():  # 스택이 가득 차 있는 경우
            raise FixedStack.Full  # 예외처리 발생
        self.stk[self.ptr] = value
        self.ptr = self.ptr + 1

    # 스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)
    def pop(self) -> Any:
        if self.is_empty():  # 스택이 비어 있음
            raise FixedStack.Empty  # 예외처리 발생
        self.ptr = self.ptr - 1
        return self.stk[self.ptr]

    # 스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)
    def peek(self) -> Any:
        if self.is_empty():  # 스택이 비어 있음
            raise FixedStack.Empty  # 예외처리 발생
        return self.stk[self.ptr - 1]

    # 스택을 비움(모든데이터를 삭제)
    def clear(self) -> None:
        self.ptr = 0

    # 스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)
    def find(self, value: Any) -> int:
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기부터 선형 검색
            if self.stk[i] == value:
                return i  # 검색성공
        return -1  # 검색실패

    # 스택에 있는 value의 개수를 반환
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr):  # 바닥부터 선형 검색
            if self.stk[i] == value:  # 검색 성공
                c = c + 1
        return c

    # 스택에 value가 있는지 판단
    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    # 스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력(덤프)
    def dump(self) -> None:
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])