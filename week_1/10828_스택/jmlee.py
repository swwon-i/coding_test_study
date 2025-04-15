#시간:44ms 메모리:34456KB
import sys

class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if not self.stack:  # 스택이 비어 있으면 -1 
            return -1
        return self.stack.pop()  # 스택에서 마지막 요소 제거하고 반환 (O(1))
    def size(self):
        return len(self.stack)  # 스택의 크기 반환 (O(1))
    def empty(self):
        return 1 if not self.stack else 0  # 스택이 비어 있으면 1, 아니면 0 (O(1))
    def top(self):
        if self.stack:  # 스택이 비어 있지 않으면
            return self.stack[-1]  # 스택의 마지막 요소 반환 (O(1))
        return -1  # 스택이 비어 있으면 -1
    def push(self, value):
        self.stack.append(value)  # 스택의 뒤쪽에 값 추가 (O(1))


lines = [line.strip() for line in sys.stdin.readlines()][1:] #0번째의 n값은 제거
stack = Stack()  

for x in lines:
    if x == 'pop':
        print(stack.pop())  # pop 명령 처리
    elif x == 'size':
        print(stack.size())  # size 명령 처리
    elif x == 'empty':
        print(stack.empty())  # empty 명령 처리
    elif x == 'top':
        print(stack.top())  # top 명령 처리
    else:  # 'push x' 명령
        stack.push(x.split()[1])  # x 값을 스택에 추가