from collections import defaultdict
import networkx as nx

with open("input.py") as f:
    ls = f.read().strip().split("\n")

G = nx.grid_2d_graph(len(ls), len(ls[0]))
heights = {(i, j): int(ls[i][j]) for i, j in G.nodes}
edges = nx.bfs_edges(G, heights)
print (heights)

#     trees = []
#     count = 0
#     for row in grid:
#         for i in range (1, len(row)-1): #for every item in the row
#             currentnum = row[i]
#             for j in range (i+1, len(row)-1): #for every item after the previous item, through to the end of row
#                 nextnum = row[j]
#                 if currentnum > nextnum:
#                     trees.append(i)
#
# print (trees)



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