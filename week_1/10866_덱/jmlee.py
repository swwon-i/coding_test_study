#시간:64ms 메모리: 35004KB
import sys
from collections import deque

class Deque:
    def __init__(self):
        self.deque = []
    def pop_front(self):
        if not self.deque:  # 덱이 비어 있으면 -1 
            return -1
        return self.deque.pop(0)  # 덱의 맨 앞 요소 제거하고 반환 
    def pop_back(self):
        if not self.deque:  # 덱이 비어 있으면 -1 
            return -1
        return self.deque.pop()  # 덱의 맨 뒤 요소 제거하고 반환 
    def size(self):
        return len(self.deque)  # 덱의 크기 반환 
    def empty(self):
        return 1 if not self.deque else 0  # 덱이 비어 있으면 1, 아니면 0 
    def front(self):
        if self.deque:  # 덱이 비어 있지 않으면
            return self.deque[0]  # 덱의 맨 앞 요소 반환 
        return -1  # 덱이 비어 있으면 -1
    def back(self):
        if self.deque:  # 덱이 비어 있지 않으면
            return self.deque[-1]  # 덱의 맨 뒤 요소 반환 
        return -1  # 덱이 비어 있으면 -1
    def push_front(self, value):
        self.deque.insert(0, value)  # 덱의 앞쪽에 값 추가 
    def push_back(self, value):
        self.deque.append(value)  # 덱의 뒤쪽에 값 추가 


lines = [line.strip() for line in sys.stdin.readlines()][1:] #0번째의 n값은 제거
deque = Deque()  

for x in lines:
    if x == 'pop_front':
        print(deque.pop_front())  # pop 명령 처리
    elif x == 'pop_back':
        print(deque.pop_back())
    elif x == 'size':
        print(deque.size())  # size 명령 처리
    elif x == 'empty':
        print(deque.empty())  # empty 명령 처리
    elif x == 'front':
        print(deque.front())  # front 명령 처리
    elif x == 'back':
        print(deque.back())  # back 명령 처리
    else:
        if x.split()[0] == 'push_front':  # 'push_front x' 명령
            deque.push_front(x.split()[1])  # x 값을 덱에 추가
        else:
            deque.push_back(x.split()[1]) # x 값을 덱에 추가