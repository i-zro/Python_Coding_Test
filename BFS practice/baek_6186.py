import sys
from collections import deque

r,c = list(map(int, sys.stdin.readline().rstrip().split()))
check = [[0]*c for i in range(r)]
matrix = [list(sys.stdin.readline().rstrip()) for i in range(r)]

q = deque()
checker = 0
def sol(i, j):
    ans = 0
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx = x + dx
            ny = y + dy

            if nx == r-1 and ny == c-1:
                break

            if 0 <= nx < r and 0 <= ny < c:
                if matrix[nx][ny] =='#' and check[nx][ny] == 0:
                    q.append((nx, ny))
                    check[nx][ny] = 1
                    ans += 1
    return ans

check[0][0] = 1

for i in range(r):
    for j in range(c):
        if check[i][j] == 0:
            ans = sol(i, j)
            if ans != 0:
                checker += 1

print(checker)