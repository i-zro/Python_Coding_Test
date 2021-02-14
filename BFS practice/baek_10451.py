import sys
sys.setrecursionlimit(2000)

def dfs(e, check, path):
    if check[e]:
        return
    check[e] = 1
    dfs(path[e]-1, check, path)

for i in range(int(sys.stdin.readline().rstrip())):
    length = int(sys.stdin.readline().rstrip())
    path = list(map(int, sys.stdin.readline().rstrip().split()))
    check = [0] * length
    result = 0

    for j in range(length):
        if check[j] == 0:
            dfs(j, check, path)
            result += 1

    print(result)
