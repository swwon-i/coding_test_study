#36264KB	1180ms
import sys
n, k = sys.stdin.readline().strip().split(' ')
k = int(k)
items = []

for _ in range(int(n)):
    w, v = map(int, sys.stdin.readline().strip().split(' '))
    items.append((w,v))
max_bag = [0] * (k+1)

def bag(k):
    for w, v in items:
        for i in range(k, w-1, -1):
            max_bag[i] = max(max_bag[i], max_bag[i-w] + v)
            
bag(k)
print(max_bag[k])