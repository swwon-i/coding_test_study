import sys 
input = sys.stdin.readline
nodes = int(input()) 
graph = [[]  for _ in range(nodes+1)]
diameter = [-1] * (nodes +1) # 지름값 

for _ in range (nodes -1):
    root, child, weight = map(int, input().split())
    graph[root].append((child, weight))
    graph[child].append((root, weight))


def dfs(start_node):
    global diamete
    stack = [] 
    stack.append((start_node, 0)) 
    diameter[start_node] = 0 
    
    while stack:
        current_node, distance = stack.pop()
        for child_node, w  in graph[current_node]:
            if diameter[child_node] == -1 :
                diameter[child_node] = distance + w  
                stack.append((child_node, distance + w))
            
    
dfs(1)
max_distance = max(diameter)
max_node = diameter.index(max_distance)
diameter = [-1] * (nodes +1) # disameter 초기화 
dfs(max_node)               
print(max(diameter))
