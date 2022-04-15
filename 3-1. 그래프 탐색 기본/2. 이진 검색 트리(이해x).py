import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break


def post_order(left, right):
    if left > right:
        return
    root = nums[left]
    left_start = left + 1
    right_end = right
    right_start = right + 1                 # 오른쪽 서브트리가 없을 수 있기 때문에 바로 재귀를 종료하는 조건을 걸어준다.

    for i in range(right - left + 1):       # 오른쪽 서브트리의 시작점을 잡는 루프 시작
        if i == 0:
            continue
        if nums[left+i] > root:
            right_start = left+i
            break
    left_end = right_start - 1

    post_order(left_start, left_end)        # 왼쪽 서브트리 재귀 시작
    post_order(right_start, right_end)      # 오른쪽 서브트리 재귀 시작
    print(root)                             # 루트 노드 출력


post_order(0, len(nums)-1)


# 전회 순회한 결과로 이진 트리를 만들어 그 이진 트리를 다시 후회 순회하여 출력하는 방법
# O(n^2) 시간복잡도로 시간 초과가 난다.

""" import sys
sys.setrecursionlimit(10**6)

class Node :
    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data


def insert_node(parents, data):
    if data <= tree[parents].data :
        if tree[parents].left is None:
            tree[parents].left = data
            tree[data] = Node(data, None, None)
        else:
            insert_node(tree[tree[parents].left].data, data)
    else:
        if tree[parents].right is None:
            tree[parents].right = data
            tree[data] = Node(data, None, None)
        else:
            insert_node(tree[tree[parents].right].data, data)

def postorder(node):
    if not node.left is None:
        postorder(tree[node.left])
    if not node.right is None:
        postorder(tree[node.right])
    print(node.data)

tree ={}

nums = []
while True:
    try:
        num = int(sys.stdin.readline())
        nums.append(num)
    except:
        break

tree[nums[0]] = Node(nums[0], None, None)

for i in range(1, len(nums)):
    insert_node(nums[0], nums[i])

postorder(tree[nums[0]]) """