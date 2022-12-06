import re
from collections import defaultdict

with open("input.py") as f:
    stacks, moves = f.read().rstrip().split("\n\n") #split into two named sections
    crates = defaultdict(list)
    crates2 = defaultdict(list)
    for s in stacks.split('\n')[:-1][::-1]:
        i = 1
        while i < len(s):
            if s[i] != ' ':
                crates[(i+3)//4].append(s[i])
                crates2[(i + 3) // 4].append(s[i])
            i += 4

def convertInstruction(move):
    reMove = [int(s) for s in re.findall(r'\d+', move)]
    vol, start, end = reMove[0], reMove[1], reMove[2]
    return (vol, start, end)

for move in moves.split('\n'):
    instruction = convertInstruction(move)
    for i in range(instruction[0]):
        crates[instruction[2]].append(crates[instruction[1]].pop())
    crates2[instruction[2]].extend(crates2[instruction[1]][-instruction[0]:]) #extend it by -x til the end
    crates2[instruction[1]] = crates2[instruction[1]][:-instruction[0]] #chop it

answer1 = ''.join(c[-1] for c in crates.values())
answer2 = ''.join(c[-1] for c in crates2.values())

print (f'solution 1 answer is {answer1}')
print (f'solution 1 answer is {answer2}')
