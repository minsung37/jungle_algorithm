import sys
input = sys.stdin.readline


# 최대공약수(Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(n * m // gcd(n, m))