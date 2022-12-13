import networkx as nx
with open('input.py') as f:
    ls = f.read().strip().split("\n")
    #map letters to numbers
    lines = [list(map(int, [(ord(x) - 96) if x.islower() else (ord(x) - 38) for x in line])) for line in ls]

G = nx.grid_2d_graph(len(lines), len(lines[0]))
heights = {(i, j): (lines[i][j]) for i, j in G.nodes}

steps = (nx.shortest_path_length(G, (0,0), (2,5)))

print (steps)


