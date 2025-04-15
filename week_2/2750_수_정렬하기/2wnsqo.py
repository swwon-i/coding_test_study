# 32412KB	36ms
import sys
n= int(sys.stdin.readline().strip())

list1 = []
for _ in range(n):
    list1.append(int(sys.stdin.readline().strip()))
list1.sort()

for l in list1:
    print(l)

# bubble
# import sys
# n= int(sys.stdin.readline().strip())
# temp = 0
# list1 = []
# for _ in range(n):
#     list1.append(int(sys.stdin.readline().strip()))
# # print('---------------')
# for i in range(len(list1)):
#     for j in range(len(list1)-i-1):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]

# for l in list1:
#     print(l)

# select
# import sys
# n= int(sys.stdin.readline().strip())
# list1 = []
# for _ in range(n):
#     list1.append(int(sys.stdin.readline().strip()))
# # print('---------------')

# # 하나씩 선택
# for i in range(len(list1)):
#     min = list1[i]
#     index = i
#     # 탐색
#     for j in range(i+1,len(list1)):
#         if min > list1[j]:
#             min = list1[j]
#             index = j
#     list1[i], list1[index] = list1[index], list1[i]

# for l in list1:
#     print(l)

# insert
# import sys
# n= int(sys.stdin.readline().strip())
# list1 = []
# for _ in range(n):
#     list1.append(int(sys.stdin.readline().strip()))
# # print('---------------')
# for i in range(1,len(list1)):
#     # range(start, stop, step)
#     for j in range(i - 1, -1, -1):  # i-1부터 0까지 거꾸로
#         if list1[i] > list1[j]:
#             list1.insert(j+1, list1.pop(i))
#             break
#     else: # for문이 break으로 끝나지 않으면 실행, 파이썬에만 있다
#         list1.insert(0, list1.pop(i))

# for l in list1:
#     print(l)

# quick
# import sys
# n= int(sys.stdin.readline().strip())
# list1 = []
# for _ in range(n):
#     list1.append(int(sys.stdin.readline().strip()))
# # print('---------------')

# def sort1(list):
#     index = len(list) //2
#     pivot = list[index]
#     list2 = []
#     list3 = []
#     middle = []
#     for i in range(len(list)):
#         if list[i] < list[index]:
#             list2.append(list[i])
#         elif list[i] > list[index]:
#             list3.append(list[i])
#         else:
#             middle.append(list[i])

#     if len(list2) >= 2:
#         left = sort1(list2)
#     else:
#         left = list2
#     if len(list3) >= 2:
#         right = sort1(list3)
#     else:
#         right = list3
#     return left + middle + right

# result = sort1(list1)
# for r in result:
#     print(r)

# merge
# import sys
# n= int(sys.stdin.readline().strip())
# list1 = []
# for _ in range(n):
#     list1.append(int(sys.stdin.readline().strip()))
# # print('---------------')


# def sort1(listt):
#     right = []
#     left = []
#     result = []
#     if len(listt) < 2:
#         return listt
    
#     index = len(listt) // 2

#     left = sort1(listt[:index])
#     right = sort1(listt[index:])

#     l ,r = 0 ,0
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l +=1
#         else:
#             result.append(right[r])
#             r +=1
    
#     result.extend(left[l:])
#     result.extend(right[r:])

#     return result

# result = sort1(list1)
# for r in result:
#     print(r)

# heap
# import sys
# n= int(sys.stdin.readline().strip())
# list1 = []
# for _ in range(n):
#     list1.append(int(sys.stdin.readline().strip()))


# def heap(listt):
#     n = len(listt)

#     for i in range(n//2 -1, -1, -1): # 절반만 0까지 -1씩씩
#         # 리스트, 부모 인덱스, 어디까지 할지
#         heap_sort(listt, i, n)
    
#     for j in range(n-1,0, -1): # n부터 1까지 -1씩
#         listt[0], listt[j] = listt[j], listt[0]
#         heap_sort(listt,0,j)

#     return listt


# def heap_sort(listt, index, n):
#     small = index
#     left = 2*index +1
#     right = 2*index +2

#     if left < n and listt[left] > listt[small]:
#         small = left
#     if right < n and listt[right] > listt[small]:
#         small = right
    
#     if small != index:
#             listt[small], listt[index] = listt[index], listt[small]
#             heap_sort(listt,small,n)
# result = heap(list1)
# for r in result:
#     print(r)
