import sys
from collections import defaultdict
import heapq

## 각 노드에서 X까지의 거리
def sol1(dic,X,ans):
    for i in range(1,len(ans)+1):
        if i == X:
            continue

        visited = set([i])
        tree = dic.copy()
        que = list(tree[i])
        heapq.heapify(que)
        while True:
            time, to_node = heapq.heappop(que)
            visited.add(to_node)
            if to_node == X:
                ans[i-1] = time
                break

            for w,v in tree[to_node]:
                if v not in visited:    
                    heapq.heappush(que, (w+time,v))
    return ans
## X에서 각 노드까지의 거리
def sol2(dic,X,ans):
    tree = dic.copy()
    que = list(tree[X])   # tree[X]를 복사해서 que에 넣어
    heapq.heapify(que)

    while que:
        time, to_node = heapq.heappop(que)
        ans[to_node-1] = min(ans[to_node-1], time)
        
        if ans[to_node - 1] == time:
            for w,v in tree[to_node]:
                heapq.heappush(que, (w+time,v))
    return ans

N, M, X = map(int, sys.stdin.readline().split())

dic = defaultdict(list)
dic2 = defaultdict(list)

answer1 = [float('inf') for _ in range(N)] # 각 노드에서 X
answer2 = [float('inf') for _ in range(N)] # X에서 각 노드

answer1[X-1] = 0
answer2[X-1] = 0

for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())    
    dic[u].append( (w,v) )
    dic2[v].append( (w,u) )

# sol1(dic,X,answer1)
sol2(dic,X,answer1)
sol2(dic2,X,answer2)

answer = [ x+y for x,y in zip(answer1, answer2)]
print(max(answer))