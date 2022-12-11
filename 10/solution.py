from collections import defaultdict
with open("input.py") as f:
    ls = [x.strip() for x in f.readlines()]

    #Function to list the lit pixels
    def markPixel(CRT, X):
        if CRT==X-1 or CRT==X or CRT==X+1:
            litpixels.append(CRT)

    signals = defaultdict(int)
    litpixels = []
    X = 1
    cycle = 0
    CRT = -1

    for l in ls:
        match l.split():
            case ["noop"]:
                cycle += 1
                if CRT < 39:
                    CRT +=1
                else:
                    CRT = 0
                markPixel(CRT, X)
                signals[cycle] = (cycle * X)

            case [_, y]:
                cycle += 1
                if CRT < 39:
                    CRT += 1
                else:
                    CRT = 0
                markPixel(CRT, X)
                signals[cycle] = (cycle * X)
                cycle += 1
                if CRT < 39:
                    CRT += 1
                else:
                    CRT = 0
                markPixel(CRT, X)
                signals[cycle] = (cycle * X)
                X += int(y)

items = {k: v for k, v in signals.items() if k in [20, 60, 100, 140, 180, 220]}

print (f'Solution 1 answer is {sum(items.values())}')
print (f'Solution 1 answer is {litpixels}')

