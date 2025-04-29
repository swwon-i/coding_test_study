# 문제 가장오래 걸리는 학생의 소요시간을 출력 
import sys 
import heapq

input = sys.stdin.readline
INF = float('inf')
N, M, X =  map(int, input().split())
graph = [[] for _ in range(N+1)]
reuslt = [] 

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0 
    heaq = []
    heapq.heappush(heaq, (0,start)) # 거리와 노드 

    while heaq:
        dist, current_node = heapq.heappop(heaq) 
        if distance[current_node] < dist: 
            continue
        
        for nearby_node, cost in graph[current_node]:
            if distance[nearby_node] > dist + cost:
                distance[nearby_node] = dist + cost 
                heapq.heappush(heaq, (dist+ cost, nearby_node))
    return distance

# 현위치에서 X 로 가는 거리
x_to = [0] * (N+1) 
for i in range (1, N+1):
    distance = dijkstra(i)
    x_to[i] = distance[X]

# X에서 다시 i로 가는 거리 
from_x = dijkstra(X)
result = [x_to[i] + from_x[i] for i in range(1, N+1)]
print(max(result))