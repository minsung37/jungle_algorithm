# 가장앞에 등장한 -를 기준으로 나눈다. => (앞에꺼) - (뒤에꺼)
expression = list(map(str, input().split('-')))
first = expression[0]
expression.remove(expression[0])

# 첫항
if "+" in first:
    temp = list(map(int, first.split("+")))
    front = sum(temp)
else:
    front = int(first)

# 두번째항부터
second = []
for i in range(len(expression)):
    if "+" in expression[i]:
        temp = list(map(int, expression[i].split("+")))
        second = second + temp
    else:
        second.append(int(expression[i]))
back = sum(second)
print(front - back)

# 가장앞에 등장한 -를 기준으로 나눈다.
# (앞에꺼) - (뒤에꺼)