import sys
import heapq
from collections import defaultdict

def sol(tree, answer, node):
    que = tree[node]
    heapq.heapify(que)

    while que:
        time, from_node, to_node = heapq.heappop(que)

        answer[from_node][to_node] = min(answer[from_node][to_node], time)
        if answer[from_node][to_node] == time:
            for w, u, v in tree[to_node]:
                val = (u,v)
                # visited.add(val)
                heapq.heappush(que, (w+time,u,v))

        print(answer)
        print(que)
    return answer

def sol2(answer):
    number = len(answer)

    for n in range(number):
        answer[n][n] = 0
    for k in range(number):
        for i in range(number):
            for j in range(number):
                if answer[i][k] + answer[k][j] < answer[i][j]:
                    answer[i][j] = answer[i][k] + answer[k][j]
    return answer

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

answer = [ [float('inf') for i in range(N)] for _ in range(N) ] 

network = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    # network[u-1].append( (w,u-1,v-1) )
    answer[u-1][v-1] = min(answer[u-1][v-1], w)

answer = sol2(answer)

for x in answer:
    for y in x:
        if y == float('inf'):
            y = 0
        print(y, end=' ')
    print()