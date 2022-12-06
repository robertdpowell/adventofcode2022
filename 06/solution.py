with open("input.py") as f:
    groups = []
    sequence = f.read()
    chars = list(sequence)
    groupedchars = [chars[i:i + 4] for i in range(0, len(chars[:-3]))]

    for group in groupedchars:
        groups.append(group)

    print (groups)
    counter = 0
    for g in groups: #for every set of 4 in the list
        while (len(g) != len(set(g))): #keep iterating until we find a group of 4 without duplicates
            counter += 1
            print(f'{g} {set(g)} {len(g)} {len(set(g))}') #debugging
            break
    counter = counter + 4 # add 4 to jump ahead to the index we want
    print (counter)

# Input examples
# mjqjpqmgbljsphdztnvjfqwrcgsmlb = 7 my solution works
# bvwbjplbgvbhsrlpgdmjqwftvncz = 5 doesn't work
# nppdvjthqldpwncqszvftbrmjlhg = 6 works
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg = 10 doesn't work
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw = 11 works