import math

with open("input.py") as f:
    forest = [list(map(int, line.strip())) for line in f.readlines()]

    num_of_rows = len(forest)
    num_of_cols = len(forest[0])
    scenics = []

    def calc_scenic(forest, row, col):
        tree_scores = []
        if col == 0 or col == num_of_cols-1 or row == 0 or row == num_of_rows-1:
            return 0

        for x in range(1, row+1):
            if (forest[row - x][col] >= forest[row][col]):
                break
        up = x
        tree_scores.append(up)

        for x in range(1, num_of_rows - row):
            if (forest[row + x][col] >= forest[row][col]):
                break
        down = x
        tree_scores.append(down)

        for x in range(1, col+1):
            if (forest[row][col - x] >= forest[row][col]):
                break
        left = x
        tree_scores.append(left)

        for x in range(1, num_of_cols - col):
            if (forest[row][col + x] >= forest[row][col]):
                break
        right = x
        tree_scores.append(right)

        scenic_score = math.prod(tree_scores)
        return scenic_score


    def is_visible(forest, row, col):
        #outside
        if col == 0 or col == num_of_cols-1 or row == 0 or row == num_of_rows-1:
            return 1
        #left
        if all(forest[row][x] < forest[row][col] for x in range(col)):
            return 1
        #right
        if all(forest[row][x] < forest[row][col] for x in range(col+1, num_of_cols)):
            return 1
        #up
        if all(forest[x][col] < forest[row][col] for x in range(row)):
            return 1
        #down
        if all(forest[x][col] < forest[row][col] for x in range(row+1, num_of_rows)):
            return 1
        return 0

    visibletrees = 0
    for row in range(num_of_rows):
        for col in range(num_of_cols):
            visibletrees += is_visible(forest, row, col)
            val = calc_scenic(forest, row, col)
            scenics.append(val)

print (f'solution 1 answer is {visibletrees}') #https://www.youtube.com/watch?v=5EKcLnuNt2k
print (f'solution 2 answer is {max(scenics)}')