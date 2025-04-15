#시간:236ms 메모리:56604KB
import sys
lines = [line.strip() for line in sys.stdin.readlines()]
X, Y = lines[0], lines[1]

def LCS_DP(X,Y): #문자열 X, 문자열 Y
    m,n = len(X), len(Y)
    table = [[None]*(n+1) for _ in range(m+1)] #빈 테이블 생성
    for i in range(m+1):
        for j in range(n+1):
            if (i == 0) or (j == 0): #기반 상황: 둘 중 하나의 문자열 길이가 0
                table[i][j] = 0
            elif X[i-1] == Y[j-1]: #일반 상황 (1): 마지막 문자가 같다
                table[i][j] = table[i-1][j-1] + 1
            else: #일반 상황 (2): 마지막 문자가 다르다
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[i][j]

print(LCS_DP(X,Y))