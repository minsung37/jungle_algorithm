import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards_array = [input().rstrip() for _ in range(n)]
array = set()


def makecard(count, permutation, visit):
    global cards_array
    if count == k:
        array.add(''.join(permutation))
        return
    for idx in range(n):
        if not visit[idx]:
            visit[idx] = 1
            makecard(count + 1, permutation + [cards_array[idx]], visit)
            visit[idx] = 0


makecard(0, [], [0] * n)
print(len(array))