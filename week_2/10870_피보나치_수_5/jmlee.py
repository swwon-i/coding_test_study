#시간:32ms 메모리:32412KB
def fibonacci(n):
    if n <= 1:
        return n
    f = [None]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

import sys
num = int(sys.stdin.readline())
print(fibonacci(num))