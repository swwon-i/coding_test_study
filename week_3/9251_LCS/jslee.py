A = input().strip()
B = input().strip()

n = len(A)
m = len(B)

# dp[i][j] = A의 앞 i글자와 B의 앞 j글자의 LCS 길이
dp = [[0] * (m + 1) for _ in range(n + 1)]

'''
dp = []
for _ in range(n + 1):
    row = [0] * (m + 1)
    dp.append(row)
'''

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:  # 현재 문자가 같으면 공통 수열이 +1
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 다르면 이전 선택 중 더 긴 것으로 회귀
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
