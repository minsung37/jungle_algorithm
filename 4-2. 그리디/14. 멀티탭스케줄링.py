import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))
plug, count = [], 0

for i in range(k):
    # 플러그에 없을때 꽂기
    if array[i] not in plug:
        # 꽉 찬경우 빼고 꽂기
        if len(plug) == n:
            for j in plug:
                # j가 꽂을 번호에 없을때
                if j not in array[i:k]:
                    plug.remove(j)
                    plug.append(array[i])
                    count = count + 1
                    break
            # 둘다 있는 경우 => 나중에 오는걸 빼야함
            else:
                # 뽑으면 안되는 애들 순서대로 담기
                plug_temp = []
                for x in array[i:k]:
                    for y in plug:
                        if x == y and x not in plug_temp:
                            plug_temp.append(x)
                plug.remove(plug_temp[-1])
                plug.append(array[i])
                count = count + 1
        # 플러그에 꽂기
        else:
            plug.append(array[i])
print(count)