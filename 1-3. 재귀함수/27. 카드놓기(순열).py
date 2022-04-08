import sys
import itertools
input = sys.stdin.readline

# 카드수, 선택수, 카드에 적힌수 입력받기
n = int(input())
k = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))

# 순열구하기
nPr = itertools.permutations(cards, k)
selectd_cards = list(nPr)

# 수 만들어서 배열에 넣기
numbers = []
for i in selectd_cards:
    temp = ""
    for j in i:
        temp = temp + str(j)
    numbers.append(temp)

# 중복제거
numbers = set(numbers)

# 만들 수 있는 정수의 개수 출력
print(len(numbers))