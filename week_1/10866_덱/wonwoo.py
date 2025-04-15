# 시간: 80ms, 메모리: 35168KB
import sys
from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()
    def push_front(self, item):
        self.deque.appendleft(item)
        return None
    def push_back(self, item):
        self.deque.append(item)
        return None
    def is_empty(self):
        if len(self.deque) == 0:
            return 1
        return 0
    def pop_front(self):
        if self.is_empty() == 1:
            return -1
        return self.deque.popleft()
    def pop_back(self):
        if self.is_empty() == 1:
            return -1
        return self.deque.pop()
    def size(self):
        return len(self.deque)
    def front(self):
        if self.is_empty() == 1:
            return -1
        return self.deque[0]
    def back(self):
        if self.is_empty() == 1:
            return -1
        return self.deque[-1]
input = sys.stdin.readlines
d = Deque()
for query in input()[1:]:
    if query.split()[0] == 'push_front':
        d.push_front(int(query.split()[1]))
    if query.split()[0] == 'push_back':
        d.push_back(int(query.split()[1]))
    if query.split()[0] == 'pop_front':
        print(d.pop_front())
    if query.split()[0] == 'pop_back':
        print(d.pop_back())
    if query.split()[0] == 'size':
        print(d.size())
    if query.split()[0] == 'empty':
        print(d.is_empty())
    if query.split()[0] == 'front':
        print(d.front())
    if query.split()[0] == 'back':
        print(d.back())

    