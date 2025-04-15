# 33432kb 48ms
import sys

n = int(sys.stdin.readline().strip())  # 첫 번째 입력: 명령 개수
stack = []  # 스택 역할을 할 리스트

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == "push":
        stack.append(command[1])  # push X → X를 스택에 추가
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if not stack else 0)
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
