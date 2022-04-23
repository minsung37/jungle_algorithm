array = input().split('-')
result = 0
for i in array[0].split('+'):
    result = result + int(i)
# 마이너스 기준으로 모두빼줌
for i in array[1:]:
    for j in i.split('+'):
        result = result - int(j)
print(result)