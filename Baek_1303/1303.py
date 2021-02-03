from collections import deque

nums = input().rstrip()
M, N = map(int, nums.split())

# N*M 매트릭스 만들기
matrix = [list(input().strip()) for i in range(N)]
check = [[0]*M for i in range(N)]

# 큐 만들기
q = deque()
w_po, b_po = 0, 0

def sol(i, j, c):
    q.append((i, j))
    check[i][j] = 1
    cnt = 1
    while q:
        # 큐에서 튜플을 뽑아 각 원소를 x,y에 넣어주기
        x, y = q.popleft()
        # dx, dy : 상, 하, 좌,우 표현한것
        # for문이 (1,0) 돌 때, dx에 1, dy에 1 들어감
        for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
            # nx, ny가 상, 하, 좌우의 각 x, y 값
            nx, ny = x+dx, y+dy
            # nx와 ny가 있는 값(매트릭스) 일때
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny] == matrix[x][y] and check[nx][ny] == 0:
                # check하기
                check[nx][ny] = 1
                # q에 nx와 ny append
                q.append((nx,ny))
                # cnt 증가(아군 수 증가)
                cnt+=1
    return cnt

for i in range(N):
    for j in range(M):
        if check[i][j] == 0:
            ans = sol(i, j, matrix[i][j])
            if matrix[i][j] == 'W':
                w_po += ans*ans
            else:
                b_po += ans*ans

print(w_po,b_po)

# from collections import deque
# m, n = map(int, input().split())
# a = [list(input().strip()) for _ in range(n)]
# check = [[False]*m for _ in range(n)]
# w, b = 0, 0
#
# def bfs(i, j, c):
#     q = deque()
#     q.append((i, j))
#     cnt = 1
#     check[i][j] = True
#     while q:
#         x, y = q.popleft()
#         for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if not check[nx][ny] and a[nx][ny] == c:
#                 q.append((nx, ny))
#                 check[nx][ny] = True
#                 cnt += 1
#     return cnt
#
# for i in range(n):
#     for j in range(m):
#         if not check[i][j]:
#             k = bfs(i, j, a[i][j])
#             if a[i][j] == 'W':
#                 w += k*k
#             else:
#                 b += k*k
# print(w, b)