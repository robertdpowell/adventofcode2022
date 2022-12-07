from collections import defaultdict

with open ('input.py') as f:
    ns = [x.strip() for x in f.readlines()]
    print(ns)

    for i in range(0, len(ns)):
        if (ns[i][:4] == "$ cd") and (ns[i+1][:4] == "$ ls"):
            print(ns[i],ns[i+2])
