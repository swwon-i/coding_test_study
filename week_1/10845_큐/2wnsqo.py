# 33432kb 44ms
import sys

n = int(sys.stdin.readline().strip())  # 첫 번째 입력: 명령 개수
queue = []  # 스택 역할을 할 리스트

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == "push":
        queue.append(command[1])  # push X → X를 스택에 추가
    elif command[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if not queue else 0)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

