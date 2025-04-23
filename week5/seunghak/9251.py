import sys 
input = sys.stdin.readline

words1 = input()
words2 = input()

dp = [[0] * (len(words1)) for _ in range(len(words2))]

for i in range(1, len(words2)):
    for j in range(1, len(words1)):
        if words2[i-1] == words1[j-1]:
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j-1]) # 이거 수정 
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[-1]))