import sys
from collections import deque
N,M = map(int, sys.stdin.readline().rstrip().split())
check = [[0 for i in range(M)] for j in range(N)]
matrix = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]

q = deque()
def sol(i, j):
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx = x + dx
            ny = y + dy

            if x == N-1 and y == M-1 :
                print(check[x][y])
                break

            if 0 <= nx < N and 0 <= ny < M :
                if matrix[nx][ny] == 1 and check[nx][ny] == 0:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

check[0][0] = 1
sol(0, 0)