# 32424KB	36ms
import sys
n = int(sys.stdin.readline().strip())
list1 = [0]
for i in range(n):
    list1.append(int(sys.stdin.readline().strip()))

dp_max = [0]*(n+1)
if n >= 1:
    dp_max[1] = list1[1]
if n >= 2:
    dp_max[2] = list1[1] + list1[2]


def dp(n):
    if (dp_max[n] != 0) or (n==0):
        return dp_max[n]
    if n>=3:
        dp_max[n] = max((dp(n-2)+list1[n]), (dp(n-3) + list1[n-1]+ list1[n]))
        return dp_max[n]

print(dp(n))