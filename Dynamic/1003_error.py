import sys
T = int(sys.stdin.readline().rstrip())
fib = {i : [] for i in range(40)}
fib[0].extend([1, 0])
fib[1].extend([0, 1])

index = 1

def makefib(num):
    if num > index:
        for i in range(index+1, num+1):
            fib[i].extend([fib[i-1][0]+fib[i-2][0], fib[i-1][1]+fib[i-2][1]])

    return fib[num]

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    makefib(N)
    print(fib[N][0], fib[N][1])
    if N > index:
        index = N