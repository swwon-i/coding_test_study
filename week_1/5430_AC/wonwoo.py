#시간: 200ms, 메모리: 44296KB

# # input 정보
#     # 첫째줄 전체 test case 개수
#     # 실행할 함수 (R: 뒤집기, D: 첫번째 수 버리기)
#     # 배열에 들어있는 수의 개수
#     # 배열

# # 접근
#     # 첫번째 수 버리기 위해 deque 사용
#     # readlines 1번째 값 버리기, for 구문으로 3개씩 슬라이싱하여 테스트 케이스 진행
#     # 예외 사항 확인

import sys
from collections import deque

input = sys.stdin.readlines
a = input()
num = int(a[0])
queries = a[1:]
for i in range(0, num): # 3개씩 묶어서 1개의 테스트 케이스 확인
    count = 0 # 뒤집은 횟수
    d = deque(queries[i*3+2].strip()[1:-1].split(',') if len(queries[i*3+2].strip()[1:-1])>0 else []) # 값이 []인 경우 deque를 []로 채우기
    is_break = False
    
    for func in queries[i*3].strip():
        if func == 'R':
            count+= 1 #뒤집는 횟수 기억하기
        else:
            if len(d) == 0 :
                print('error')
                is_break = True # error만 출력하기 위한 bool 값
                break 
            if count != 0 and count % 2 != 0: # 홀수번 뒤집었으면 뒤에서 지우기
                d.pop()
            else: # 짝수번 뒤집었으면 앞에서 지우기
                d.popleft()
    if not is_break: # error가 발생하지 않았을 경우
        if count != 0 and count % 2 != 0:  # 홀수번 뒤집었으면 뒤집기
            d.reverse()
        print('['+','.join(map(str,d))+']')