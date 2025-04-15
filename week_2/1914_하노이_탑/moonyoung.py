# 메모리 : 232036KB, 시간 : 332ms
import sys

N = int(sys.stdin.readline())
hanoi_list = []

def hanoi(n, start, sub, end):
    if n == 1:
        if N <= 20:
            hanoi_list.append(f"{start} {end}")
        return
    hanoi(n-1, start, end, sub)
    if N <= 20:
        hanoi_list.append(f"{start} {end}")
    hanoi(n-1, sub, start, end)
if N <= 20 :
    hanoi(N, 1, 2, 3)
else :
    pass
sys.stdout.write(str(2 ** N - 1) + "\n")

if N <= 20:
    sys.stdout.write("\n".join(hanoi_list) + "\n")
