# 용액 특성갑 입력받고 정렬하기
n = int(input())
solution = list(map(int, input().split()))
solution.sort()
# 투포인터 설정
left = 0
right = n - 1
# 0에 가까운 특성값 담을 변수
answer = 99999999999
# 그때의 두용액의 특성값을 담을 변수
result = []

# 투포인터
while left < right:
    spec_left = solution[left]
    spec_right = solution[right]
    spec = spec_left + spec_right

    # 특성값이 0에 가장 가까운 경우
    if abs(spec) < answer:
        answer = abs(spec)
        result = [spec_left, spec_right]
    if spec < 0:
        left = left + 1
    else:
        right = right - 1
# 결과출력
print(result[0], result[1])