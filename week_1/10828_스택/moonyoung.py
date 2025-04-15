# 시간: 44ms, 메모리: 33432kb
import sys

N = int(sys.stdin.readline().strip())

stack = []

for _ in range(N) :
  char = sys.stdin.readline().strip().split()
  
  if char[0] == 'push' :
    stack.append(char[1])
  elif char[0] == 'pop' :
    if len(stack) < 1 :
      print(-1)
    else: 
      print(stack.pop(-1))
  elif char[0] == 'size' :
    print(len(stack))
  elif char[0] == 'empty' :
    if len(stack) < 1 :
      print(1)
    else :
      print(0)
  elif char[0] == 'top' :
    if len(stack) < 1 :
      print(-1)
    else :
      print(stack[-1])
      