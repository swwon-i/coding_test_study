# 32412KB	660ms
import sys
n= int(sys.stdin.readline().strip())
def hanoi(n,start,sub,end):
    if n == 1:
        print(f'{start} {end}')
        return c
    hanoi(n-1,start,end,sub)
    print(f'{start} {end}')
    hanoi(n-1,sub,start,end)

c = 1
for i in range(n-1):
    c = 2*c+1
print(c)

if n<=20:
    hanoi(n,1,2,3)
