#시간: 32ms 메모리:32412KB
import sys
stairs = [int(line.strip()) for line in sys.stdin.readlines()][1:]
num = len(stairs)

def stair_climb(n,stairs):
    #계단 수가 적은 경우, 예외 처리
    if n == 1:
        return stairs[0]
    elif n == 2:
        return stairs[0] + stairs[1]
    elif n == 3:
        return max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    #dp[i]: i번째 계단까지 왔을 때의 최대 점수
    dp = [0] * (n+1)
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    
    for i in range(3,n):
        #두 가지 중 더 큰 값을 취한다
        #(1) i-2번째 -> i번째 (2칸, 1칸) (2) i-3번째 -> i-1번째 -> i번째 (2칸, 1칸, 1칸)
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
    return dp[n-1]

print(stair_climb(num, stairs))