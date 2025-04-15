# 2차원 dp: 시간: 1708ms 메모리: 135816KB
# 1차원 dp: 시간 : 200ms 메모리: 32412KB

# X_i = x라는 word의 i번째 값
# Y_j = y라는 word의 j번째 값
# S_(X_i,Y_j) = X, Y의 n번째 단어까지의 최대 공통 수열의 길이
# S_(X_i,Y_j) = 
#   X_n == Y_n:
#       S_(X_(i-1), Y_(j-1)) + 1 # 둘이 같으면 n-1 까지의 최대 공통 수열의 길이 + 1
#   X_n != Y_n:
#       max(S_((X_(i-1), Y_j), S_((X_(i)), Y_(j-1))) 
# 같지 않으면 X의 n번째, Y의 n-1번째까지의 최대 공통 수열의 길이와 X의 n-1번째, Y의 n번째까지의 최대 공통 수열의 길이 중 더 큰 값
import sys
input = sys.stdin.readline

str_1 = input().strip()
str_2 = input().strip()

# def lcs_solve(str_1, str_2):
#     dp = {'-1_-1': 0}
#     dp.update({str(a)+ '_-1' : 0 for a in range(len(str_1))})
#     dp.update({'-1_'+ str(a) : 0 for a in range(len(str_2))}) # padding처럼 배열 맨 앞에 0으로 채워넣기
#     for i in range(len(str_1)):
#         for j in range(len(str_2)):
#             current = str(i)+ '_' +str(j)
#             prev_i = str(i - 1) + '_' + str(j)
#             prev_j = str(i) + '_' + str(j - 1)
#             prev_ij = str(i - 1) + '_' + str(j - 1)
#             if str_1[i] == str_2[j]:
#                 dp[current] = dp[prev_ij] + 1
#             else:
#                 dp[current] = max(dp[prev_i], dp[prev_j])
#     return max(list(dp.values()))
# print(lcs_solve(str_1, str_2))


# 1차원 dp
dp = [0] * len(str_2)
for i in range(len(str_1)):
    start = 0
    for j in range(len(str_2)):
        if start < dp[j]:
            start = dp[j]
        elif str_1[i] == str_2[j]:
            dp[j] = start + 1
print(max(dp))