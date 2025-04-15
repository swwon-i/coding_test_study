#버블정렬 / 시간:84ms 메모리:32412KB
def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list

#공통출력
import sys
lines = [int(line.strip()) for line in sys.stdin.readlines()][1:]
# lines=[4,6,1,2,9,5,7]
bubble_sort(lines) #해당 정렬 함수 입력
#lines = merge_sort(lines) #return값이 lines가 아닌 경우
answer = ''
for num in lines:
    answer += str(num) + '\n'
print(answer)


#선택정렬 / 시간:56ms 메모리:32412KB
def selection_sort(num_list):
    n = len(num_list)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if num_list[j] < num_list[min_index]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list


#삽입정렬 / 시간:88ms 메모리:32412KB
def insertion_sort(num_list):
    n = len(num_list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if num_list[j] < num_list[j-1]:
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
    return num_list

#병합정렬 / 시간:36ms 메모리:32412KB
def merge_sort(num_list):
    n = len(num_list)
    if n < 2:
        return num_list
    mid = len(num_list)//2
    low_list = merge_sort(num_list[:mid])
    high_list = merge_sort(num_list[mid:])
    merged_list = []
    l, h = 0,0 #low_list와 high_list 현재 위치(인덱스)
    while l < len(low_list) and h < len(high_list):
        if low_list[l] < high_list[h]:
            merged_list.append(low_list[l])
            l += 1
        else:
            merged_list.append(high_list[h])
            h += 1
    merged_list += low_list[l:]
    merged_list += high_list[h:]
    return merged_list


#퀵정렬 / 시간:44ms 메모리:32544KB
def quick_sort(num_list):
    n = len(num_list)
    if n <= 1:
        return num_list
    pivot = n // 2
    front_arr, pivot_arr, back_arr = [],[],[]
    for num in num_list:
        if num < num_list[pivot]:
            front_arr.append(num)
        elif num > num_list[pivot]:
            back_arr.append(num)
        else:
            pivot_arr.append(num)
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)


#힙정렬 / 시간:44ms 메모리:32412KB
def heapify(array, index, heap_size):
    parent = index
    left = 2 * index + 1
    right = 2 * index + 2
   
    if left < heap_size and array[left] > array[parent]:
       parent = left
    if right < heap_size and array[right] > array[parent]:
       parent = right
    if parent != index:
        array[parent] , array[index] = array[index], array[parent]
        heapify(array,parent,heap_size)

def heap_sort(num_list):
    n = len(num_list)
    for i in range( n//2 -1 , -1, -1):
        heapify(num_list,i,n)
    for i in range(n-1,0,-1):
        num_list[0], num_list[i] = num_list[i], num_list[0]
        heapify(num_list,0,i)
    return num_list



