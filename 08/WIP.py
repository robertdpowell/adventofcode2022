import networkx as nx

with open("input.py") as f:
    grid = list(list(map(int,(x.strip()))) for x in f.read().split('\n'))
    print (grid)

    count = 0
    for row in grid:
        print(row)
        for i in row:
            while (row[i] < (len(row)-1)) and (row[i] > row[i+1]):
                print (i)
                count +=1
                break
    print (count)






# create a list of lists of all horizontal and vertical rows
# for i in range i to length of groid forward and backward
#     if i > i in range

#
# G = nx.grid_2d_graph(len(ls), len(ls[0]))
# for i in nx.connected_components(G):
#     print (i)
#
# heights = {(i, j): int(ls[i][j]) for i, j in G.nodes}
# #
# # print(f' solution 1 answer is {sum(heights[v] for v in G.nodes if (heights[v] > heights[u] for u in G.add_edge(v, )))}')
#
#
# # for k,v in heights.items():
#
#
# # for height in heights.items():
#     print (height + 1)

#works if higher than surrounding trees
# G.number_of_edges()