import fileinput
import re
import pytest

pairs = list(line.strip().split(',') for line in (fileinput.input(files = 'input.py')))

def convertPair(pair):
    p1 = re.sub(r'(-)', ',', pair[0])
    p2 = re.sub(r'(-)', ',', pair[1])
    p1 = list(p1.split(','))
    p2 = list(p2.split(','))
    p1 = list(map(int, p1))
    p2 = list(map(int, p2))
    p1 = (list(range(p1[0], (p1[1] + 1))))
    p2 = (list(range(p2[0], (p2[1] + 1))))
    return (p1, p2)

def solve1(pairs):
    counter = 0
    for pair in pairs:
        p1, p2 = map(set, convertPair(pair))
        if (p1.issubset(p2) or (p2.issubset(p1))):
            counter += 1
    return (counter)

def solve2(pairs):
    matches = []
    for pair in pairs:
        p1, p2 = convertPair(pair)
        for i in p2:
            p1.append(i)
        if len(p1) > len(set(p1)):
            matches.append(pair)
    return (len(matches))

print (f'solution1 answer is {solve1(pairs)}')
print (f'solution1 answer is {solve2(pairs)}')