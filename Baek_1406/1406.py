import sys
sentence = sys.stdin.readline()
sentence = sentence.rstrip()
sentlist = list(sentence)

N = int(sys.stdin.readline())
comlist = []
for i in range(N):
    command = sys.stdin.readline()
    command = command.rstrip()
    comlist.append(command)

cursor = len(sentence)
for com in comlist:
    if com[0] == 'L' and cursor > 0:
        cursor-=1
    if com[0] == 'D' and cursor < len(sentence):
        cursor+=1
    if com[0] == 'B' and cursor > 0:
        sentlist.pop(cursor-1)
        cursor -= 1
    if com[0] == 'P':
        sentlist = sentlist[:cursor]
        temp = sentlist[cursor:]
        sentlist.append(com[-1])
        sentlist.extend(temp)
        cursor += 1
        print(sentlist)
print(comlist)
output = "".join(sentlist)
print(output)