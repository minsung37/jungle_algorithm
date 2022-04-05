# 배열의 크기를 선언하고 값을 True로 초기화
limit = 1001
eratos = [True for i in range(limit)]

# 0, 1 제외(False)
eratos[0] = False
eratos[1] = False

# 소수아닌것 제외(False)
for i in range(2, int(len(eratos) ** 0.5 + 1)):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = False

for i in range(limit):
    if eratos[i]:
        print(i, end=" ")