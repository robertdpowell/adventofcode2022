from collections import defaultdict

# https://github.com/fuglede/adventofcode/blob/master/2022/day07/solutions.py
with open("input.py") as f:
    ls = [x.strip() for x in f.readlines()]
    sizes = defaultdict(int)
    cwd = []
    for l in ls:
        match l.split():
            #goes through each line, reads it and updates the list, based on the input
            case [_, _, "/"]:
                cwd = []
            case [_, _, ".."]:
                cwd.pop()
            case [_, _, x]:
                cwd.append(x)
            case [a, _] if a.isdigit():
                for i in range(len(cwd)+1): #for every dir ref in our list
                    path = "/" + "/".join(cwd[:i]) # construct path for that dir
                    sizes[path] += int(a) #create a key and add all values to that key

    totalspace = 70000000
    requiredspace = 30000000
    currentfreespace = totalspace - sizes["/"]
    needtodelete = requiredspace - currentfreespace

    print(f' solution answer 1 is {sum(filter(lambda v: v <= 100000, sizes.values()))}')
    print(f' solution answer 2 is {min(filter(lambda v: v >= (needtodelete), sizes.values()))}')



