import re

with open("input.py") as f:
    ls = [x.strip() for x in f.readlines()]
    print (len(ls))

    start_pattern = r"^\$ ls$"
    end_pattern = r"^\$ $"

    start_regex = re.compile(start_pattern)
    end_regex = re.compile(end_pattern)

    dirs = []
    dir = []
    in_dir = False

    i = 0
    while i < len(ls):
        start_match = start_regex.match(ls[i])
        end_match = end_regex.match(ls[i])

        if start_match:
            in_dir = True
            print(ls[i])
            dir.append(ls[i])
            print (dir)
            i += 1

        if end_match:
            in_dir = False
            print(ls[i])
            i += 1
            dirs.append(dir)
            dir = []



print (dirs)





    # sizes = defaultdict(int)
    # stack = []
    # for l in ls:
    #     match l.split():
    #         # case [_, _, "/"]:
    #         #     stack = []
    #         #     print (stack)
    #         # case [_, _, ".."]:
    #         #     stack.pop()
    #         #     print(stack)
    #         case [_, _, x]:
    #             stack.append(x)
    #             print(stack)
    #         case [a, _] if a.isdigit():
    #             for i in range(len(stack) + 1):
    #                 print(i)
    #                 path = "/" + "/".join(stack[:i])
    #                 sizes[path] += int(a)
    #
    # print (sizes)
    #
    #
    #
