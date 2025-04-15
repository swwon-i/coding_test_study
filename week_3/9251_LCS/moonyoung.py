## 메모리 : 57628KB, 시간 : 432ms
import sys
char_A = sys.stdin.readline()
char_B = sys.stdin.readline()
# 행 a 열 b
table = [[0]*(len(char_B)+1) for _ in range(len(char_A)+1)]

# 0으로 시작하면 인덱싱오류(음수) 나기때문에 1로 시작 
for i in range(1, len(char_A) + 1) :
    for j in range(1, len(char_B) + 1) :
        if char_A[i-1] == char_B[j-1] : # A와 B가 같으면
            table[i][j] = table[i-1][j-1] +1 # 대각선 +1
        else :
            table[i][j] = max(table[i-1][j], table[i][j-1] )
print(table[len(char_A)][len(char_B)])
