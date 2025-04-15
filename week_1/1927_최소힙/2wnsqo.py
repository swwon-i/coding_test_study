# 	38340kb 120ms
import sys
import heapq
N = int(sys.stdin.readline().strip())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        heapq.heappush(heap, num)
    else: # num == 0
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
