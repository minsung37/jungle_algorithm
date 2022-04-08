import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())
print(math.ceil((v-b) / (a-b)))

# (v-b) / (a-b)를 올림안하는 경우
#  - 정상에 도달했는데 미끄러지는경우 방지
# (v-b) / (a-b)를 올림하는 경우
#  - 다음날에 오르면 정상도달 하므로 + 1 => 올림