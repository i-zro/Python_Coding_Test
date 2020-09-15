key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 90도 회전 시키는 함수
def rotate_90(matrix):
    row = len(matrix)
    col = len(matrix[0])
    answer_matrix = [[0]*col]*row
    for i in range(row):
        for j in range(col):
            answer_matrix[i][j] = matrix[j][i]
    return answer_matrix

def solution(key, lock):
    # lock의 홈이 어디서 부터 시작해서 어디까지 가는지 확인
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
    width = max_row - min_row + 1
    height = max_col - min_col + 1
    lock_a = [[0] * width]*height
    lock_a = lock[min_row : max_row+1, min_col : max_col+1]
    rot_90 = rotate_90(lock_a)

    return rot_90

print(solution(key,lock))