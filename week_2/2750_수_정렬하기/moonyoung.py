# 메모리 : 32412KB, 시간 : 60ms

import sys

N = int(sys.stdin.readline())

list_num = []

for i in range(N) :
  num = int(input())
  list_num.append(num)

list_num.sort()

for num in list_num :
  print(num)



# 버블정렬 - 메모리 : 110728KB, 시간 : 116ms
# import sys

# N = int(sys.stdin.readline())

# list_num = []

# for i in range(N) :
#   num = int(input())
#   list_num.append(num)


# def bubble_sort(array) :
#   for i in range(len(array)) :
#       for j in range(len(array)-i-1) :
#         if array[j] > array[j+1] :
#           array[j], array[j+1] = array[j+1], array[j]
#   return array

# bubble_list = bubble_sort(list_num)

# for num in bubble_list :
#   print(num)



# 삽입정렬 - 메모리 : 110724KB, 시간 : 108ms
# import sys

# N = int(sys.stdin.readline())

# list_num = []

# for i in range(N) :
#   num = int(input())
#   list_num.append(num)

# def insert_sort(array) :
#     for i in range(1, len(array)) :
#        key = array[i]
#        j = i - 1
#        while j >= 0 and array[j] > key :
#           array[j+1] = array[j]
#           j -= 1
#        array[j+1] = key
#     return array

# insert_list = insert_sort(list_num)

# for num in insert_list :
#   print(num)



# 선택정렬 - 메모리 : 110728KB, 시간 : 112ms
# import sys

# N = int(sys.stdin.readline())

# list_num = []


# for i in range(N) :
#   num = int(input())
#   list_num.append(num)

# def select_sort(array) :
#     for i in range(len(array)) :
#        min_index = i
#        for j in range(i+1, len(array)) :
#           if array[j] < array[min_index] :
#              min_index = j
#        array[i], array[min_index] = array[min_index], array[i]
#     return array

# select_list = select_sort(list_num)

# for num in select_list :
#   print(num)



# 퀵정렬 -  메모리 : 110736KB, 시간 : 116ms
# import sys

# N = int(sys.stdin.readline())

# list_num = []


# for i in range(N) :
#   num = int(input())
#   list_num.append(num)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array

#     pivot_index = len(array) // 2
#     pivot = array[pivot_index]

#     rest = array[:pivot_index] + array[pivot_index+1:]

#     left = [x for x in rest if x <= pivot]
#     right = [x for x in rest if x > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)

# quick_list = quick_sort(list_num)

# for num in quick_list :
#   print(num)



# 병합정렬 - 시간 : 110920KB, 시간 : 120ms
# import sys

# N = int(sys.stdin.readline())

# list_num = []

# for i in range(N) :
#   num = int(input())
#   list_num.append(num)

# def merge_sort(array):
#   if len(array) <= 1 :
#     return array
#   mid = len(array) // 2
#   left = merge_sort(array[:mid])
#   right = merge_sort(array[mid:])
#   return merge(left, right)

# def merge(left, right) :
#   result = []
#   i = 0
#   j = 0
#   while i < len(left) and j < len(right) :
#     if left[i] <= right[j] :
#       result.append(left[i])
#       i += 1
#     else :
#       result.append(right[j])
#       j += 1
#   result += left[i:]
#   result += right[j:]
#   return result

# merge_list = merge_sort(list_num)

# for num in merge_list :
#   print(num)


