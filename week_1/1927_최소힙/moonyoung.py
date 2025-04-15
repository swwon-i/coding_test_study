# 시간: 120ms, 메모리: 38340kb
import heapq
import sys

N = int(sys.stdin.readline().strip())

hq = []

for _ in range(N) :
  X = int(sys.stdin.readline().strip())
  if X > 0 :
    heapq.heappush(hq, X)
  elif X == 0 :
    if len(hq) < 1 :
      print(0)
    else :
      print(heapq.heappop(hq))