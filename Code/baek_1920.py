import sys
N = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))

n_list = sorted(n_list)

def half_exp(num):
    max_idx = len(n_list)-1
    min_idx = 0
    while(min_idx <= max_idx):
        mid_idx = (max_idx + min_idx) // 2
        if n_list[mid_idx]== num:
            return 1
        elif n_list[mid_idx]>num:
            min_idx = mid_idx
        else:
            max_idx = mid_idx
    return 0

for i in m_list:
    print(half_exp(i))