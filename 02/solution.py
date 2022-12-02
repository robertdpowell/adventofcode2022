import fileinput
rounds = list(line.strip() for line in (fileinput.input(files = 'input.py')))

def solve1():
    solutionOneScore = 0
    for round in rounds:
        f, s = round.split(' ')
        f = int(f.translate(str.maketrans("ABC", "123")))
        s = int(s.translate(str.maketrans("XYZ", "123")))

        solutionOneScore += s

        if f == s:
            solutionOneScore += 3
        elif ((f == 1 and s == 2) or (f == 2 and s == 3) or (f == 3 and s == 1)):
            solutionOneScore += 6

    return solutionOneScore

def solve2():
    solutionTwoScore = 0
    for round in rounds:
        f, s = round.split(' ')
        f = int(f.translate(str.maketrans("ABC", "123")))
        s = int(s.translate(str.maketrans("XYZ", "036")))

        solutionTwoScore += s

        if ((f == 1 and s == 0) or (f == 2 and s == 6) or (f == s)):
            solutionTwoScore += 3
        elif ((f == 1 and s == 6) or (f == 2 and s == 3) or (f == 3 and s == 0)):
            solutionTwoScore += 2
        else:
            solutionTwoScore += 1
    return solutionTwoScore

print (solve1())
print (solve2())

