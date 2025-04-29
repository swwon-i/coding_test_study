# 퀸은 같은 행,열 그리고 대각선을 움직일 수 있음 
n = int(input()) 
chess_board = [-1] * n 
result = []

def is_safe(board, row, col):
    # 1. 같은열에 체스가 존재하는지 확인 
    for i in range(row):
        if board[i] == col:
            return False
    # 2. 대각선 값이 존재하는 지 확인 
    for i in range(row):
        if abs(board[i]-col) == abs(i-row):
            return False        
    return True

def n_queens(n, row, board):
    global result
    
    if row == n: # 기저함수 모든 퀸을 배치했을 경우 
        result.append(board) # 이거 대신에 카운트 증가 하면 python에서 시간초과 안나올거임,
        return 
    
    for col in range(n): #열에 대해서 찾아보기 
        if is_safe(board, row, col):
            board[row] = col
            n_queens(n, row+1, board)
            board[row] = -1 # 백트레이킹  
    
n_queens(n, 0, chess_board)

print(len(result))