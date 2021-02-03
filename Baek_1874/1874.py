import sys
N = int(sys.stdin.readline())

item = int(sys.stdin.readline())
# 처음 나온 정수로 1부터 스택 채우기
stk = [i for i in range(1, item)]
command = ["+" for i in range(item)]
command.append("-")
push_num = item # 이미 push 된 수
no = 0

for i in range(N-1):
    item = int(sys.stdin.readline())

    if(stk and item < stk[-1]):
        print("NO")
        no = 1
        break
    else:
        if (stk and item == stk[-1]):
            stk.pop(-1)
            command.append("-")
        else:
            stk.extend([i for i in range(push_num+1, item)])
            command.extend(["+" for i in range(push_num+1, item+1)])
            command.append("-")
            push_num = item

if no == 0:
    for i in command:
        print(i)
