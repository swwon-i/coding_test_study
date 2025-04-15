#시간: 68ms, 메모리: 35540KB
from collections import deque # 무작위 접근이 어려움, 맨 앞과 맨 뒤 뺄 수 있음
import sys

input = sys.stdin.readlines
cases = input()[1:]
q = deque()
# 리스트는 메모리 주소가 공유되기 때문에 리턴을 안 해도 되긴 함
def push(q, num):
    q.append(num)
    return None

def pop(q):
    if len(q) == 0:
        return -1
    
    return q.pop()

def size(q):
    return len(q)

def empty(q):
    if len(q) == 0:
        return 1
    return 0

def top(q):
    if len(q) == 0:
        return -1
    return q[-1]



for case in cases:
    case = list(case.split())
    if case[0] == 'push':
        push(q, case[1])
    if case[0] == 'pop':
        print(pop(q))
    if case[0] == 'size':
        print(size(q))
    if case[0] == 'empty':
        print(empty(q))
    if case[0] == 'top':
        print(top(q))