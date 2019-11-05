from util import Stack, Queue  # These may come in handy

q = Queue()


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
    pass
