# 원판 n개를 start에서 target으로 옮기기
def hanoi(num, start, target):
    if num > 1:
        hanoi(num - 1, start, 6 - start - target)
    print(start, target)
    if num > 1:
        hanoi(num - 1, 6 - start - target, target)


n = int(input())
print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3)
