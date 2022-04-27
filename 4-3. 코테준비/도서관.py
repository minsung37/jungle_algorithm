import sys
input = sys.stdin.readline

# 책 위치입력 받아서 양수음수 나눠서 담고 정렬
n, m = map(int, input().split())
books = list(map(int, input().split()))
positive_books, negative_books, count = [0], [0], 0
for i in books:
    if i > 0:
        positive_books.append(i)
    else:
        negative_books.append(-i)
positive_books.sort()
negative_books.sort()
# 처음 가는곳인지 체크
first = True


# 걸음수 카운트
def sol(books):
    global count, first
    books.remove(0)
    k = len(books)
    # 한번에 옮겨지는 경우
    if 0 < k <= m:
        if first:
            count = count + books[-1] * 2
        else:
            count = count + books[-1]
    # 여러번 가는경우
    else:
        for i in range((k - 1) % m, k - 1, m):
            count = count + books[i] * 2
        if k > 0:
            if first:

                count = count + books[-1] * 2
            else:
                count = count + books[-1]
    first = False


# 작은쪽을 먼저 방문
if max(negative_books) > max(positive_books):
    sol(positive_books)
    sol(negative_books)
else:
    sol(negative_books)
    sol(positive_books)
print(count)