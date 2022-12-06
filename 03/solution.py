with open('input.py') as f:
    bps = [x.strip() for x in f.readlines()]
    groupedbps = [bps[i:i+3] for i in range(0, len(bps), 3)]
    print (groupedbps)

    def convert(matches):
        # The ord() function returns the number representing the unicode code of a specified character.
        # Subtract 96 and 38 from lower and upper case unicode values respectively to align with priority pattern outlined in puzzle
        prio = list(map(int, [(ord(x)-96) if x.islower() else (ord(x)-38) for x in matches]))
        return (sum(prio))

    def solve1():
        matches = []
        for i in bps:
            # split in half and remove the duplicates
            h1 = set(i[:len(i) // 2])
            h2 = set(i[len(i) // 2:])
            for i in h1:
                for j in h2:
                    if i == j:
                        matches.append(i)
        return (convert(matches))

    def solve2():
        matches = []
        for group in groupedbps:
            first = set(group[0])
            second = set(group[1])
            third = set(group[2])
            for i in first:
                for j in second:
                    for k in third:
                        if i == j == k:
                            matches.append(i)
        return (convert(matches))

print (f' Solution 1 answer is {solve1()}')
print (f' Solution 2 answer is {solve2()}')



