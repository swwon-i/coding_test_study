# 시간 : 36ms, 메모리 : 32412 KB
# N : 전체 계단 개수
# n : 현재 위치한 계단
# X_n : 현재 위치한 계단의 점수
# S_n : 현재 위치한 계단까지의 누적 점수

# 점화식 S_n = max((S_(n-2) + X_(n-1) + X_n), S_(n-1) + X_n))
import sys
input = sys.stdin.readlines()

N = int(input[0])
step = list(map(int,input[1:]))

dp = {0 : 0, 1 : step[0]}


def step_raise(index):
    if index in dp.keys():
        return dp[index]
    x_n = step[index - 1]
    if index == 2:
        dp[index] = dp[index-1] + x_n
        
    elif index >= 3 :
        s_n_2 = step_raise(index - 3) 
        s_n_1 = step_raise(index - 2)
        
        dp[index] = max(s_n_2 + step[index - 2] + x_n , s_n_1 + x_n)
    return dp[index]

print(step_raise(N))

