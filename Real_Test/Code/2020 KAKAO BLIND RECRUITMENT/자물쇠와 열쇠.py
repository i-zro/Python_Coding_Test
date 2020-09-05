key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key, lock):
    # 홈이 어디서 부터 시작해서 어디까지 가는지 확인
    min_row, max_row, min_col, max_col = -1, -1, -1, -1
    n = len(lock) # lock 가로 길이
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                if min_row==-1:
                    min_row,max_row = j, j
                else:
                    if j<min_row:
                        min_row=j
                    elif j>max_row:
                        max_row=j
                    else:pass
                if min_col==-1:
                    min_col, max_col = i, i
                else:
                    if i<min_col:
                        min_col=i
                    elif i>max_col:
                        max_col=i
                    else:pass
    row_length=max_row - min_row + 1
    col_length=max_col - max_col + 1



    answer = True
    return answer

solution(key, lock)