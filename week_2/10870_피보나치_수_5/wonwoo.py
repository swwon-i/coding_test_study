# 시간: 36ms, 메모리: 32412KB
# 시간: 36ms, 메모리: 32412KB 동일
# [0, 1] 기본 값
# fn = fn-2 + fn-1
# f1 = 0 + 1
# f2 = 1 + f1
# f3 = f1 + f2
import sys

input = sys.stdin.readline
fibonacci_list = []
num = int(input())

# def fibonacci_numbers(num, i): # 피보나치 함수(몇번째, 0부터 증가하는 수)
#     if num < i: i가 num까지 갔을 경우, 정답을 보여주는 조건문
#         return fibonacci_list[-1]
#     fibonacci_list.append(i if i < 2 else fibonacci_list[i-2] + fibonacci_list[i-1]) # 0번쨰와 1번째일 경우 그냥 그 값을 넣고, 2번째부터는 앞, 앞앞 값을 더해서 넣기
#     i += 1
#     return fibonacci_numbers(num, i) # 반복

# print(fibonacci_numbers(num, 0))

def fibonacci_numbers(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci_numbers(num-1) + fibonacci_numbers(num-2)

print(fibonacci_numbers(num))