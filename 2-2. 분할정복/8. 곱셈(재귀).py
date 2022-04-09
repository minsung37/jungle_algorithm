a, b, c = map(int, input().split())


# (a ** n) % c
def sol(a, b):
    if b == 1:
        return a % c
    else:
        if b % 2 == 0:
            return (sol(a, b // 2) ** 2) % c
        else:
            return ((sol(a, b // 2) ** 2) * a) % c


print(sol(a, b))
# 나머지 분배법칙
# (A * B) % C = (A % C) * (B % C) % C