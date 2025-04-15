N = int(input())

print(2**N - 1)

if N <= 20:
    def hanoi(n, start, end, temp):
        if n == 1:
            print(f"{start} {end}")
            return
        hanoi(n-1, start, temp, end)
        print(f"{start} {end}")
        hanoi(n-1, temp, end, start)

    hanoi(N, 1, 3, 2)