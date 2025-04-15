## 메모리 : 36264KB, 시간 : 1352ms
import sys
N, K = map(int, sys.stdin.readline().split())
weight = [] # 무게들을 리스트로 저장
value = [] # 가치들을 리스트로 저장
value_dp = [0] * (K + 1) # 최대가치를 구하기 위해 무게+1만큼 0의 리스트를 만들기

for _ in range(N) :
  W, V = map(int, sys.stdin.readline().split())
  weight.append(W) 
  value.append(V) 

def max_value(K) :
  for i in range(N) :
    for j in range(K, weight[i] -1, -1): # K부터 weight[i]를 빼면서 역순으로
      # 역순으로 하는 이유 -> 중복 방지
      value_dp[j] = max(value_dp[j], value_dp[j - weight[i]] + value[i] )
  return value_dp[K]

print(max_value(K))
