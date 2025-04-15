# 39404kb 276ms
import sys
from collections import deque
N = int(sys.stdin.readline().strip())
for _ in range(N):
    numbers = []
    rc = 0
    result = 0
    c = sys.stdin.readline().strip() # 명령
    n = sys.stdin.readline().strip() # 단어수
    numbers = sys.stdin.readline().strip() # 숫자 [1,2,3,4]
    if numbers == "[]":
        numbers = deque()  # 빈 deque
    else:
        numbers = deque(map(int, numbers[1:-1].split(',')))
    for i in range(len(c)):
        if c[i] == 'R':
            rc +=1
        elif c[i] == 'D':
            if numbers:
                if rc % 2 == 0:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                print('error')
                result = 1
                break
    if rc % 2 == 1:
        numbers.reverse()
    numbers = list(numbers)
    if result == 0:
        print(f"[{','.join(map(str,numbers))}]")