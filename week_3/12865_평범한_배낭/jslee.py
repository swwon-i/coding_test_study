import sys

input = sys.stdin.readline
N, K = map(int, input().split())
weight = [0] # 안 헷갈리기 위해, 인덱스 0에 0 삽입 후 후반부에 1부터 시작
value = [0]

for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

    
dp = []
for i in range(N + 1): #무게 대비 가치 고려하는 2차원 배열을 생성
    a = [0] * (K + 1)
    dp.append(a)
    
# w - 지금 배낭에서 남은 여유 무게
for i in range(1, N + 1):        
    for w in range(K + 1):    
        if weight[i] > w: #무게가 지금 남은 가방의 무게보다 무거울 때
            dp[i][w] = dp[i-1][w] # 안 넣음
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i]) 
    #넣으면 현재 여유 무게에 weight(i)만큼 빼면서, 그 가치를 더함. 이걸 안 넣은 것과 비교해서 높은 쪽 저장
    
print(dp[N][K])

