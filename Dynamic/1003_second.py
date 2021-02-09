import sys
fib = {0 : [0,1], 1: [1,0]}
for i in range(2, 40):
    fib[i] = [fib[i-1][0] + fib[i-2][0], fib[i-1][1] + fib[i-2][1]]
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(fib[n][0], fib[n][1])