import sys
N = int(sys.stdin.readline())


for i in range(N):
    # 거꾸로 된 문장
    new_line = ""

    line = sys.stdin.readline()
    line = line.rstrip()

    # 띄어쓰기 단위로 line 리스트에 넣어주기
    word_list = line.split()

    for i in word_list:
        new_line += i[::-1]
        new_line += " "
    print(new_line)