# 32412kb 44ms
import sys

n = int(sys.stdin.readline().strip())  # 첫 번째 입력: 명령 개수
deck= []  # 스택 역할을 할 리스트

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == "push_front":
        deck.insert(0,command[1])  
    elif command[0] == "push_back":
        deck.append(command[1]) 
    elif command[0] == "pop_front":
        if deck:
            print(deck.pop(0))
        else:
            print(-1)
    elif command[0] == "pop_back":
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deck))
    elif command[0] == "empty":
        print(1 if not deck else 0)
    elif command[0] == "front":
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif command[0] == "back":
        if deck:
            print(deck[-1])
        else:
            print(-1)
