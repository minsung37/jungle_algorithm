# 문제 조건 입력받기
a, b = map(str, input().split())
reversed_a = ""
reversed_b = ""

# 문자열 뒤집어서 합치기
for i in range(0, 3):
    x = a[2 - i]
    y = b[2 - i]
    reversed_a = reversed_a + x
    reversed_b = reversed_b + y

# 큰값 출력
print(max(int(reversed_a), int(reversed_b)))
