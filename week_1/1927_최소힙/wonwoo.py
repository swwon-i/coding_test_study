# 시간:116ms, 메모리:46824KB
import sys
import heapq

input = sys.stdin.readlines

class Heapq():
    def __init__(self):
        self.heap = []
    def append(self, num):
        heapq.heappush(self.heap, num)
    def pop(self):
        if len(self.heap) == 0:
            return 0
        temp = heapq.heappop(self.heap)
        return temp

h = Heapq()
for query in input()[1:]:
    if int(query) == 0:
        print(h.pop())
    else:
        h.append(int(query))