# 시간: 64ms, 메모리: 34976kb
from collections import deque
import sys

N = int(sys.stdin.readline().strip())

dq = deque([])

for _ in range(N) :
  char = sys.stdin.readline().strip().split()

  if char[0] == 'push_front' :
    dq.appendleft(char[1])
  elif char[0] == 'push_back' :
    dq.append(char[1])
  elif char[0] == 'pop_front' :
    if len(dq) < 1 :
      print(-1)
    else: 
      print(dq.popleft())
  elif char[0] == 'pop_back' :
    if len(dq) < 1 :
      print(-1)
    else: 
      print(dq.pop())
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