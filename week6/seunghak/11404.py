# 버스 정보 시작 도시, 도착 도시, 걸리는 시간 
import sys 


INF = float('inf')
input = sys.stdin.readline
city_nums = int(input())
bus_nums = int(input())
distance = [[INF] * city_nums for _ in range(city_nums)] # -1 처리 해줘야함 

# 자기 자신은 0 으로 초기화 
for i in range(city_nums):
    distance[i][i] = 0 

for _ in range(bus_nums):
    start, end, cost = map(int,input().split())
    distance[start-1][end-1] = min(distance[start-1][end-1], cost)

# 플로이드 알고리즘 
for k in range(city_nums):
    for i in range(city_nums):
        for j in range(city_nums):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 무한대인 값들 0으로 초기화 
for i in range(city_nums):
    for j in range(city_nums):
        if distance[i][j] == INF:
            distance[i][j] = 0 
# 출력 
for i in range(city_nums):
    print(*distance[i])
