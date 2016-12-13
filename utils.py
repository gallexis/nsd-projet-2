
def get_nodes_from_edge(edge):
    return edge.split(' ')

def get_nodes_from_graph(graph):
    nodesSet = set()

    for edge in graph:
        nodes = get_nodes_from_edge(edge)
        [nodesSet.add(n) for n in nodes]

    return list(nodesSet)

def size_of_graph(graph):
    nodes = get_nodes_from_graph(graph)
    return len(nodes)

def load_graph(graph):
    nodes = {}

    for edge in graph:
        ns = get_nodes_from_edge(edge)
        n0 = ns[0]

        # if node's degree == 0, empty list
        if len(ns) == 1:
            nodes[n0] = set()

        else:
            n1 = ns[1]
            # if nodes already in dict, append his new neighbour
            if n0 in nodes:
                nodes[n0].add(n1)

            # if node not yet in dict, initialise a new list & add his neighbour
            else:
                nodes[n0] = set(n1)

            # same as before, but with opposite nodes, in case there is
            # A B, but not B A
            if n1 in nodes:
                nodes[n1].add(n0)
            else:
                nodes[n1] = set(n0)

    return nodes

def delete_loop(loadedGraph):
    for node in loadedGraph:
        if node in loadedGraph[node]:
            loadedGraph[node].remove(node)

    return loadedGraph

def get_max_degree_nodes(loadedGraph):
    return len( max(loadedGraph.values()) )


########
def empty_adjacency_matrix_from_graph(graph):
    nodes = get_nodes_from_graph(graph)
    matrix = {}

    for node in nodes:
        matrix[node] = []

    return matrix


def link_exists(node1, node2, graph):
    nodes = graph[node1]
    return node2 in nodes


def add_link(node1, node2, simul):
    simul[node1].append(node2)
    simul[node2].append(node1)


def write_line(file, test_number, node1, node2):
    file.write(str(test_number) + ' ' + str(str(node1) + " " + str(node2) + "\n"))
