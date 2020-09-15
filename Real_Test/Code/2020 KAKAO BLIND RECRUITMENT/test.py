lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate_90(matrix):
    row = len(matrix)
    col = len(matrix[0])
    answer_matrix = [[0]*col]*row
    for i in range(row):b
        for j in range(col):
            answer_matrix[i][j] = matrix[j][row-i]
    return answer_matrix


'''def essential_lock(lock):
    check = 0
    while (check>4):
        if lock[0].count(1) == len(lock[0]):
            lock.pop(0)
            check = 0
        else:
            check+=1
        lock = rotate_90(lock)

print(essential_lock(lock))'''

print(rotate_90(lock))