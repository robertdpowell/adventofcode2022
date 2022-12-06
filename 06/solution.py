with open("input.py") as f:
    chars = list(f.read().strip())

    def compute(num):
        head = num
        for c in chars:
            while (len(chars[head-num:head])) != (len(set(chars[head-num:head]))):
                head += 1
                break
        return (head)

print (f'solution 1 answer is {compute(4)}')
print (f'solution 2 answer is {compute(14)}')

