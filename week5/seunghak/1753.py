import sys 
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
start_edge = int(input())

distance = [float('INF')] * (V+1)
graph = [[]  for _ in range(V+1)] # 초기화 

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    

def dijkstra(graph, source): # source = 출발지점 
    q = [] 
    distance[source] = 0 
    heapq.heappush(q, (0, source))
    while q:
        dist, current_v = heapq.heappop(q)
        if distance[current_v] < dist:
            continue
        
        for neighbor_v, neighbor_dist in graph[current_v]:
            cost = distance[current_v] + neighbor_dist
            if cost < distance[neighbor_v]:
                distance[neighbor_v] = cost
                heapq.heappush(q, (cost, neighbor_v))

dijkstra(graph, start_edge)

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])