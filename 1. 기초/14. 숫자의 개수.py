a = int(input())
b = int(input())
c = int(input())
num = str(a * b * c)

# 0 ~ 9 등장 횟수 찾기
for i in range(10):
    # 문자열에서 일치하는문자 찾기
    print(num.count(str(i)))