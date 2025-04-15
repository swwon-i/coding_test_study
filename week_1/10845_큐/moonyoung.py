# 시간: 72ms, 메모리: 34944kb
from collections import deque
import sys

N = int(sys.stdin.readline().strip())

dq = deque([])

for _ in range(N) :
  char = sys.stdin.readline().strip().split()

  if char[0] == 'push' :
    dq.append(char[1])
  elif char[0] == 'pop' :
    if len(dq) < 1 :
      print(-1)
    else: 
      print(dq.popleft())
  elif char[0] == 'size' :
    print(len(dq))
  elif char[0] == 'empty' :
    if len(dq) < 1 :
      print(1)
    else :
      print(0)
  elif char[0] == 'front' :
    if len(dq) < 1 :
      print(-1)
    else :
      print(dq[0])
  elif char[0] == 'back' :
    if len(dq) < 1 :
      print(-1)
    else :
      print(dq[-1])