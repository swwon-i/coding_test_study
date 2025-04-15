#시간:808ms 메모리:32412KB
import sys
num = int(sys.stdin.readline())

def hanoi_tower(n,start,temp,end):
    if (n==1):
        print(start, end)
        return
    else:
        hanoi_tower(n-1, start, end, temp)
        print(start, end)
        hanoi_tower(n-1, temp, start, end)

print(2 ** num - 1)
if num <= 20:
    hanoi_tower(num,1,2,3)