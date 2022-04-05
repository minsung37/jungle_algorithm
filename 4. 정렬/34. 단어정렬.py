import sys
input = sys.stdin.readline

# 단어입력받기
n = int(input())
words = []
for i in range(n):
    word = input().rstrip()
    words.append(word)

# 단어 중복제거
words = list(set(words))

# [길이, 단어] 구조로 배열 만들고 정렬하기
result = []
for i in words:
    result.append([len(i), i])
result.sort()

# 정답출력
for i in result:
    print(i[1])
