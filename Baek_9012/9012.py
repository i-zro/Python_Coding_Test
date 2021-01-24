import sys
N = int(sys.stdin.readline())

def VPS(sentence):
    replaced = sentence.replace("()","")
    if replaced == sentence:    # 탈출조건
        if replaced == "":
            print("YES")
            return
        else:
            print("NO")
            return
    else:
        VPS(replaced)

for i in range(N):
    sentence = sys.stdin.readline()
    sentence = sentence.rstrip()
    VPS(sentence)