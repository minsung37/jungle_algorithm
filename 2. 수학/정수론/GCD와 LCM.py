# n, m = map(int, input().split())
n, m = 24, 18


# 최대공약수(Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#  a  b
# 24 18
# 18  6
#  6  0 => 반복문 종료 6 리턴


# 최소공배수(Least Common Multiple)
def lcm(a, b):
    return a * b // gcd(a, b)


# 24 18 => 6 72
print("최대공약수 :", gcd(n, m))
print("최소공배수 :", lcm(n, m))
