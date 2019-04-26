from Graph import Graph
artist = 'searchformeaning'
load_graph = True


graph = Graph()
if load_graph:
    graph.load(artist + ".dat")
else:
    graph.generate_graph_from_file(artist + ".txt")
    graph.save(artist + ".dat")
print(graph.generate_sentence())
