import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 전위순회 결과
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break


# 후위순회
def postorder(start, end):
    if start > end:
        return
    root = preorder[start]
    index = start + 1

    # root보다 커지는 index 찾기
    while index <= end:
        if root < preorder[index]:
            break
        index = index + 1

    # 왼쪽 서브트리
    postorder(start + 1, index - 1)
    # 오른쪽 서브트리
    postorder(index, end)
    # 출력
    print(root)


postorder(0, len(preorder) - 1)