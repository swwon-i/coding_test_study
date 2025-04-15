# 시간: 44ms, 메모리: 32412KB

import sys
input = sys.stdin.readlines
num_list = input()[1:]

num_list.sort(key = lambda x : int(x))
print(''.join(num_list))

# Bubble Sort
# for j in range(len(num_list) - 1): # 리스트 전체를 순환(마지막 값은 x)
#     for index in range(len(num_list) - 1 - j): # 리스트의 값을 앞에서부터 돌면서, 비교하기
#         if int(num_list[index]) > int(num_list[index + 1]): 앞에 값이 뒤의 값보다 큰 경우 자리 체인지
#             num_list[index] , num_list[index + 1] = num_list[index + 1], num_list[index]


# Select Sort
# for index in range(len(num_list)): # 리스트 전체를 순환
#     min_index = index # 순환문의 index를 기준 index로 설정 -> 뒤의 값들이 더 작은 경우 min_index를 변경
#     for j in range(index + 1, len(num_list)): # 기준 index보다 큰 index와 비교하기
#         if num_list[min_index] > num_list[j]: # 만약 index가 기준 index보다 크면 min_index를 변경
#             min_index = j
#     num_list[index], num_list[min_index] = num_list[min_index], num_list[index] # 변경 작업
# print(''.join(num_list))

# Insert Sort
# for index in range(1, len(num_list)): # 밑의 값부터 확인
#     key = int(num_list[index]) # index에 해당하는 값을 기준으로 설정
#     a= index - 1
#     while a >= 0 and int(num_list[a]) < key: # index보다 작은 애들과 비교하여, key값이 더 크면 바꾸기
#         num_list[a+1] = num_list[a] 
#         a -= 1
#     num_list[a+1] = key
# print(num_list)

# # Quick Sort -> 일부 값을 지정하여 그 값보다 작은지 큰지 확인
# def quick_sort(array): 
#     if len(array) < 2: 
#         return array
    
#     select = int(array[len(array) // 2]) # 임의의 기준점 (중간값으로 표현)
#     big = []
#     equal = []
#     small = []
#     for num in array: # 설정한 기준점보다 값이 큰지 확인
#         if int(num) > select:
#             big.append(num)
#         elif int(num) < select:
#             small.append(num)
#         else:
#             equal.append(num)
#     return quick_sort(small) + equal + quick_sort(big)

# print(''.join(quick_sort(num_list)))

# Merge Sort -> 반을 나눠서 진행
# def merge_sort(array): 
#     if len(array) < 2:
#         return array
    
#     merge_array = []
    
#     mid = len(array) // 2 # 기준점 잡기
#     big = merge_sort(array[mid:]) # array의 절반을 나눠서 각 두개의 array에 대해 정렬 진행행
#     small = merge_sort(array[:mid])
    
#     big_index = 0
#     small_index = 0
    
#     while big_index < len(big) and small_index < len(small) : # 기준점보다 크거나 작은 array 중 한개라도 끝에 도달하면 멈춤
#         if big[big_index] > small[small_index]:
#             merge_array.append(big[big_index])
#             big_index += 1
#         else:
#             merge_array.append(small[small_index])
#             small_index += 1
#     merge_array += big[big_index:] # 남은 값들을 추가하기
#     merge_array += small[small_index:]
#     return merge_array

# print(merge_sort(num_list))


# # Heap Sort

# def heap_array(array, length): # 힙 정렬을 위한 힙 구조 만들기
#     for index in range(len(array) -1 - length , 0, -1): # 맨 밑에 해당하는 값부터 부모 노드와 값을 비교
#         parent_node = (index - 1) // 2 # 부모 노드를 구하는 공식
#         if int(array[parent_node]) < int(array[index]): # 부모 노드보다 값이 작으면 자리 체인지
#             temp = array[index] # 바꾸기 위해 array[index] 현재 인덱스에 해당하는 값을 지정
#             array[index] = array[parent_node] # 자리 바꾸기기
#             array[parent_node] = temp
#     return array

# def heap_sort(array, length): # 마지막 값을 계속 제외하기 위해 length 변수 추가
#     if length == len(array) - 1: # length 값이 array의 길이의 -1과 같으면 즉 배열이 1개 남았을 때, return
#         return array
#     array = heap_array(array, length) # 힙 구조 돌기
#     temp = array[0] # 맨 위의 값 임시 저장
#     array[0], array[-1 - length] = array[-1 - length], temp # 맨 위의 값과 비교 대상의 제일 밑의 값과 변경
#     length += 1
#     return heap_sort(array, length)
# print(''.join(heap_sort(num_list, 0)))