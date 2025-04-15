#시간:1732ms 메모리:230376KB 
import sys
lines = [list(map(int,line.strip().split())) for line in sys.stdin.readlines()]
n, max_w = lines[0][0], lines[0][1]
items = lines[1:] #item_w, item_v

def Knapsack(items,max_w):
    n = len(items)
    dp = [[0] * (max_w + 1) for _ in range(n+1)]
    #dp[i][w]: i번째 아이템까지 고려했을 때, 무게 w 이하로 담을 수 있는 최대 가치
    for i in range(1, n + 1):
        weight, value = items[i - 1] 
        for w in range(max_w + 1): #가능한 가방 무게 (0 ~ max_w)까지 탐색
            if weight > w: #가방에 공간이 없는 경우: 이전 상태 유지
                dp[i][w] = dp[i - 1][w]
            else: #가방에 공간이 있어서, 아이템을 담거나 담지 않았을 때의 최대 가치를 택한다
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    return dp[n][max_w]

Knapsack(items,max_w)