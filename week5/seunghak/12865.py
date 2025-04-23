# 무게 가치 = (w, v) limited_weight = K
import sys 
input = sys.stdin.readline
items =[(0,0)]
number_items, limited_weight = map(int, input().split())
dp = [[0] * (limited_weight+1) for _ in range(number_items+1)] # weight, value qoduf 

for _ in range(number_items):
    weight, value = map(int, input().split())
    items.append((weight, value))

for i in range(1, number_items+1):
    for k in range(1, limited_weight+1):
        if   items[i][0] > k:
            dp[i][k] = dp[i-1][k]
        else:  
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-items[i][0]] + items[i][1])

print(dp[number_items][limited_weight])