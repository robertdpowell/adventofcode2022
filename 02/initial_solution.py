import fileinput
rounds = list(word.strip() for word in (fileinput.input(files = 'input.py')))

firstScore = 0
secondScore = 0

def calculateRound(round):
    if 'A Y' in round:
        return 8
    elif 'A X' in round:
        return 4
    elif 'A Z' in round:
        return 3
    elif 'B Y' in round:
        return 5
    elif 'B X' in round:
        return 1
    elif 'B Z' in round:
        return 9
    elif 'C Y' in round:
        return 2
    elif 'C X' in round:
        return 7
    elif 'C Z' in round:
        return 6

def calculateRoundAgain(round):
    if 'A Y' in round:
        return 4
    elif 'A X' in round:
        return 3
    elif 'A Z' in round:
        return 8
    elif 'B Y' in round:
        return 5
    elif 'B X' in round:
        return 1
    elif 'B Z' in round:
        return 9
    elif 'C Y' in round:
        return 6
    elif 'C X' in round:
        return 2
    elif 'C Z' in round:
        return 7

for round in rounds:
    firstScore += (calculateRound(round))
    secondScore += (calculateRoundAgain(round))

print (f'solution 1 answer = {(firstScore)}')
print (f'solution 1 answer = {(secondScore)}')