import sys
import heapq
from collections import defaultdict

def sol(tree,node,ans):
    ans[node] = 0
    que = list(tree[node])
    heapq.heapify(que)
    index, value = 1, 0
    
    while que:
        weight, to_node = heapq.heappop(que)
        if len(ans) == 3:
            return to_node, weight
        
        ans[to_node] = min(ans[to_node], weight)
        
        if ans[to_node] == weight:
            for w,v in tree[to_node]:
                heapq.heappush(que, (w+weight,v))
                if value < weight:
                    value = weight
                    index = to_node
        
    #  while que:
    #     time, to_node = heapq.heappop(que)
    #     ans[to_node-1] = min(ans[to_node-1], time)
        
    #     if ans[to_node - 1] == time:
    #         for w,v in tree[to_node]:
    #             heapq.heappush(que, (w+time,v))
    
    return index, value

N = int(sys.stdin.readline())
M = N + 1

answer1 = [ float('inf')  for _ in range(M)]  
answer2 = [ float('inf')  for _ in range(M)]  
tree = defaultdict(list)

for _ in range(N-1):
    u, v, w = map(int, sys.stdin.readline().split())
    tree[u].append((w,v))
    tree[v].append((w,u))

id1, val1 = sol(tree,1,answer1)
id2, val2 = sol(tree,id1,answer2)

print(val2)