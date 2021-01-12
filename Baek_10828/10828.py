import sys

# 명령의 수
N = int(sys.stdin.readline())

# 스택
stack = []

# push
def push(X):
    stack.append(X)

# pop
def pop():
    if stack:
        print(stack.pop(-1))
    else:
        print(-1)

# top
def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

for i in range(N):
    # 출력해야하는 명령
    command = sys.stdin.readline()
    command = command.rstrip()
    if command[1] == 'o' : #pop, top 두 개 있음
        if command[0] == 'p':
            pop()
        else:
            top()
    elif command[3] == 'h' : #push 밖에 없음
        push(command[5:])
    elif command[0] == 's':
        size()
    else :
        empty()