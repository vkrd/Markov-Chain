from Graph import Graph
file = 'data/shakespeare'
load_graph = False

graph = Graph()


if load_graph:
    # load graph
    graph.load(file + ".dat")
else:
    # create graph from text file
    graph.generate_graph_from_file(file + ".txt")

    # save graph
    graph.save(file + ".dat")

# generate and print an example statement
print(graph.generate_sentence())
