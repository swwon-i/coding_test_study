#57628KB	440ms
import sys
text1 = sys.stdin.readline().strip()
text2 = sys.stdin.readline().strip()

text1_len = len(text1)
text2_len = len(text2)
result = [[0] * text1_len for _ in range(text2_len)]
max_num = 0
for i in range(text1_len):
    if text1[i] == text2[0]:
        result[0][i] = 1
    elif (i >=1) and (result[0][i-1] == 1):
        result[0][i] = 1

for j in range(text2_len):
    if text2[j] == text1[0]:
        result[j][0] = 1
    elif (j >=1) and (result[j-1][0] == 1):
        result[j][0] = 1

for i in range(1, text1_len):
    for j in range(1, text2_len):
        if text1[i] == text2[j]:
            max_num = result[j-1][i-1] +1
        else:
            max_num = max(result[j-1][i],result[j][i-1])
        result[j][i] = max_num

# 단어가 n개지만 n+1이 될수도 있다
# for i in range(1, text1_len):
#     for j in range(1, text2_len):
#         if text1[i] == text2[j]:
#             max_num = max(result[j-1][i],result[j][i-1]) +1
#         else:
#             max_num = max(result[j-1][i],result[j][i-1])
#         result[j][i] = max_num

print(result[text2_len-1][text1_len-1])
