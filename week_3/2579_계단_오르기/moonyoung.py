## 메모리 : 32412KB, 시간 : 32ms
import sys
N = int(sys.stdin.readline())
score = [] # 계단에 쓰인 점수
max_score = [0] * N # 최고값 비교할 리스트

for i in range(N) :
  score_num = int(sys.stdin.readline())
  score.append(score_num) # 점수 받아서 저장

if N == 1 : # 첫 번째 계단은 첫 번째 값이 최대
  max_score[0] = score[0]
elif N == 2 : # 두 번째 계단은 첫 번째와 두 번째의 합이 최대
  max_score[1] = score[0] + score[1]
else :
  max_score[0] = score[0]
  max_score[1] = score[0] + score[1]
  # 세 번째 계단은 1->3, 2->3 중 최대
  max_score[2] = max(max_score[0] + score[2], score[1] + score[2] )
  for i in range(3, N) : # 그 이후의 계단은 i-2 -> i와 i-3 -> i-1 -> i 중 최대
    max_score[i] = max(max_score[i-2] + score[i], max_score[i-3] + score[i-1] + score[i])
  
print(max_score[N-1])