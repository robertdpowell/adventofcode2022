from collections import defaultdict

with open("input.py") as f:
    ls = [x.strip() for x in f.readlines()]

    for line in ls:
        parts = line.strip().split(' ')
        if parts[0].isdigit():
            print(parts[0])



    # dirs = defaultdict()
    # path = []
    # for line in ls:
    #     match line:
    #         case["$", "cd", name]:
    #             path.append(name)
    #
    #     print(path)
    #     #
        #
        #
        # if l.startswith('$ cd'):
        #     x = l[5:] #get the key
        #     if x.islower():
        #         print(x)
        # #
        # if l[0].isdigit():
        #     print (l)
        #

    # # for i in range(0, len(ns)):
    # #     if (ns[i][:4] == "$ cd") and (ns[i+1][:4] == "$ ls"):
    # #         print(ns[i],ns[i+2])
    #
    # for i in range(0, len(ns)):
    #     if (ns[i][:1]).isnumeric():
    #         print (ns[i-2])
    #         print (ns[i - 2])

