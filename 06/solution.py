with open("input.py") as f:
    chars = list(f.read())
    groupedchars = [chars[i:i + 4] for i in range(0, len(chars[:-3]))]
    counter = 4
    for g in groupedchars:
        while (len(g) != len(set(g))):
            counter += 1
            break
    print (counter)

# Input examples-
# mjqjpqmgbljsphdztnvjfqwrcgsmlb = 7 my solution works
# bvwbjplbgvbhsrlpgdmjqwftvncz = 5 doesn't work
# nppdvjthqldpwncqszvftbrmjlhg = 6 works
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg = 10 doesn't work
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw = 11 works