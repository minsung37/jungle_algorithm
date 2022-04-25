import sys
input = sys.stdin.readline

n, k = map(int, input().split())
plug = list(map(int, input().split()))
tap, count = [], 0

for i in range(k):
    # 멀티탭에 없을때 꽂기
    if plug[i] not in tap:
        # 꽉 찬경우 플러그 빼고 꽂기
        if len(tap) == n:
            for j in tap:
                # j가 더이상 안쓰일때 뽑는다
                if j not in plug[i:k]:
                    tap.remove(j)
                    tap.append(plug[i])
                    count = count + 1
                    break
            # 둘다 있는 경우 => 나중에 오는걸 빼야함
            else:
                # 우선순위 순으로 스택에 담기
                tap_temp = []
                for x in plug[i:k]:
                    for y in tap:
                        if x == y and x not in tap_temp:
                            tap_temp.append(x)
                # 우선순위 마지막을 탭에서 뽑기
                tap.remove(tap_temp[-1])
                tap.append(plug[i])
                count = count + 1
        # 플러그에 꽂기
        else:
            tap.append(plug[i])
print(count)