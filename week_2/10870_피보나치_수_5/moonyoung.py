# 메모리 : 32412KB, 36ms
import sys
N = int(sys.stdin.readline())

def fibonacci(n) :
  if n == 0 :
    return 0
  elif n == 1 :
    return 1
  else :
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(N))