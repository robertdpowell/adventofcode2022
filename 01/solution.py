with open("input.py") as f:
    calories = []
    for line in f.read().split("\n\n"): #split the list into groups separated by blank lines
        elf = list(map(int, line.split("\n"))) #convert each string in group into ints
        elfCals = sum(elf) #sum each group
        calories.append(elfCals) #add each sum to a list

calories.sort(reverse=True)
maxThree = sum(calories[:3])

print (f'solution 1 answer is {(max(calories))}')
print (f'solution 2 answer is {(maxThree)}')
