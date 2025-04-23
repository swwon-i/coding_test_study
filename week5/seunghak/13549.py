# 걷거나 순간이동이 가능함 
# X 위치에서 걸을 경우 1초 뒤에 x-1, 또는 x+1 으로 갈수 있음 
# 순간이동시에는 0초에서 2*X으로 넘어갈 수 있음 
from collections import deque
import sys
input = sys.stdin.readline 
max_len = 100_001
process_time = [999999] * max_len  

subin_loc, bro_loc = map(int, input().split())
# 현재 위치는 0으로 설정 
process_time[subin_loc] = 0
# bfs 구성 # 현재위치에서 순간이동 후 좌우로 위치를 판단 +1
def bfs(current_loc, target_loc):
    global process_time, visited
    queque = deque()
    queque.append(current_loc)
    
    while queque:
        current_loc = queque.popleft()
        if current_loc == target_loc: 
            break 
        teleport = current_loc * 2 
        if 0 <= teleport < max_len and process_time[teleport] > process_time[current_loc]+1:
            process_time[teleport] = process_time[current_loc]
            queque.appendleft(teleport)
            
        for teleport in [current_loc-1, current_loc+1]:
            if 0 <= teleport < max_len and process_time[teleport] > process_time[current_loc] +1:
                process_time[teleport] = process_time[current_loc] + 1 # 이동 후 걸린시간 
                queque.append(teleport)

                    
bfs(subin_loc, bro_loc)
print(process_time[bro_loc])
                
            

    