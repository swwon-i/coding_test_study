# 시간: 76ms, 메모리: 35392KB
from collections import deque
import sys
class Queue:
    def __init__(self):
        self.queue = deque()
    def push(self, item):
        self.queue.append(item)
        return None
    
    def is_empty(self):
        if len(self.queue) == 0:
            return 1
        return 0

    def pop(self):
        if self.is_empty():
            return -1
        return self.queue.popleft()
    def size(self):
        return len(self.queue)
    def front(self):
        if self.is_empty() == 1:
            return -1
        return self.queue[0]
    def back(self):
        if self.is_empty() == 1:
            return -1
        return self.queue[-1]

input = sys.stdin.readlines    


queue = Queue()

for query in input()[1:]:
    if query.split()[0] == 'push':
        queue.push(int(query.split()[1]))
    if query.split()[0] == 'pop':
        print(queue.pop())
    if query.split()[0] == 'size':
        print(queue.size())
    if query.split()[0] == 'empty':
        print(queue.is_empty())
    if query.split()[0] == 'front':
        print(queue.front())
    if query.split()[0] == 'back':
        print(queue.back())

