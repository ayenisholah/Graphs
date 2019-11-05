class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """
        Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
            Add a vertex to the graph
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
            Add a directed edge to the graph
        """
        # Check if v1 and v2 exists in vertices list
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 at v1 of vertices
            self.vertices[v1].add(v2)
        # Otherwise
        else:
            # Raise and error
            raise KeyError("That vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # load pairs to graph
    for parents in ancestors:
        graph.add_vertex(parents[0])
        graph.add_vertex(parents[1])

    #   {1 : {3}, 2: {3}, 3: {6}, 4: {5, 8}, 5: {6, 7}, 6: {}, 7:{} 8: {9}, 9:{}, 10: {1}, 11: {8}}

    # edges

