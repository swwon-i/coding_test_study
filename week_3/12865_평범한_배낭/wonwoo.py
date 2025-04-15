# 시간: 4168ms 메모리: 229352KB
import sys

input = sys.stdin.readlines()

N, k = map(int,input[0].strip().split())
weight_value = [list(map(int, line.split())) for line in input[1:]]

dp = [[0] * (k + 1)for i in range(N + 1)]

for i in range(1, N + 1):
    w, v = weight_value[i - 1]
    for j in range(1, k + 1): # 부피
        
        if j < w: # 지금 부피가 가능한 부피보다 더 큰 경우 
            dp[i][j] = dp[i - 1][j] # 바로 전 값을 가져오기기
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + weight_value[i - 1][1]) #  바로 전값, (지금 값을 넣었을 떄 나머지 부피에 대한 최대값 + 지금 값)의 최대 값값
print(max(max(dp)))