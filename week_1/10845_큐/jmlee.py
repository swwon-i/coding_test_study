#시간:44ms 메모리: 34456KB
import sys

class Queue:
    def __init__(self):
        self.queue = []
    def pop(self):
        if not self.queue:  # 큐가 비어 있으면 -1 
            return -1
        return self.queue.pop(0)  # 큐에서 맨 앞 요소 제거하고 반환 (O(1))
    def size(self):
        return len(self.queue)  # 큐의 크기 반환 (O(1))
    def empty(self):
        return 1 if not self.queue else 0  # 큐가 비어 있으면 1, 아니면 0 (O(1))
    def front(self):
        if self.queue:  # 큐가 비어 있지 않으면
            return self.queue[0]  # 큐의 맨 앞 요소 반환 (O(1))
        return -1  # 큐가 비어 있으면 -1
    def back(self):
        if self.queue:  # 큐가 비어 있지 않으면
            return self.queue[-1]  # 큐의 맨 뒤 요소 반환 (O(1))
        return -1  # 큐가 비어 있으면 -1
    def push(self, value):
        self.queue.append(value)  # 큐의 뒤쪽에 값 추가 (O(1))


lines = [line.strip() for line in sys.stdin.readlines()][1:] #0번째의 n값은 제거
queue = Queue()  

for x in lines:
    if x == 'pop':
        print(queue.pop())  # pop 명령 처리
    elif x == 'size':
        print(queue.size())  # size 명령 처리
    elif x == 'empty':
        print(queue.empty())  # empty 명령 처리
    elif x == 'front':
        print(queue.front())  # front 명령 처리
    elif x == 'back':
        print(queue.back())  # back 명령 처리
    else:  # 'push x' 명령
        queue.push(x.split()[1])  # x 값을 큐에 추가