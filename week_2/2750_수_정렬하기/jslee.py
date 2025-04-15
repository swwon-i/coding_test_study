import sys
input = sys.stdin.readline

# 입력
n = int(input())  # 첫 줄: 숫자 개수
arr = []

for _ in range(n):
    arr.append(int(input().strip())) #숫자 입력받기

#정렬 함수들 정의

#버블
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#선택               
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#삽입        
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#퀵
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right) #left, right 리스트를 새로 만들어서 재귀로 붙인 후 리턴

#피벗
def pivot_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    pivot_sort(arr, start, right - 1)
    pivot_sort(arr, right + 1, end)

# === 여기서 정렬 알고리즘 하나 골라 실행 ===

# 1. 버블 정렬
# bubble_sort(arr)

# 2. 선택 정렬
# selection_sort(arr)

# 3. 삽입 정렬
# insertion_sort(arr)

# 4. 퀵 정렬 (새 리스트 리턴하므로 덮어쓰기!)
# arr = quick_sort(arr)

# 5. 피벗 정렬
# pivot_sort(arr, 0, len(arr) - 1)

arr.sort()  # 오름차순 정렬

#출력
for num in arr:
    print(num)
