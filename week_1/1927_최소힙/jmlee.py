#시간:128ms 메모리:49364KB
import sys
import heapq

lines = [line.strip() for line in sys.stdin.readlines()][1:] #0번째의 n값은 제거
Q = []

for x in lines:
    if int(x) == 0:
       if len(Q) == 0:
           print(0)
       else:
           print(heapq.heappop(Q))
    else:
        heapq.heappush(Q, int(x))

