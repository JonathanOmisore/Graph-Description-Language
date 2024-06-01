from  Graph import Graph
class GraphDLInterpreter:
    def __init__(self):
        self.graphs = {}
    
    def execute(self, command):
        parts = command.split()
        if parts[0] == "create" and parts[1] == "graph":
            graph_name = parts[2]
            self.graphs[graph_name] = Graph()
        elif parts[0] == "add" and parts[1] == "vertex":
            vertex_name = parts[2]
            graph_name = parts[4]
            self.graphs[graph_name].add_vertex(vertex_name)
        elif parts[0] == "add" and parts[1] == "edge":
            from_vertex = parts[2]
            to_vertex = parts[4]
            graph_name = parts[6]
            self.graphs[graph_name].add_edge(from_vertex, to_vertex)
        elif parts[0] == "neighbors" and parts[1] == "of":
            vertex_name = parts[2]
            graph_name = parts[4]
            neighbors = self.graphs[graph_name].neighbors(vertex_name)
            print(f"Neighbors of {vertex_name} in {graph_name}: {neighbors}")
        elif parts[0] == "is" and parts[1] == "connected":
            from_vertex = parts[2]
            to_vertex = parts[4]
            graph_name = parts[6]
            connected = self.graphs[graph_name].is_connected(from_vertex, to_vertex)
            print(f"Is {from_vertex} connected to {to_vertex} in {graph_name}: {connected}")
        elif parts[0] == "is" and parts[1] == "empty":
            graph_name = parts[2]
            empty = self.graphs[graph_name].is_empty()
            print(f"Is {graph_name} empty: {empty}")
        elif parts[0] == "degree" and parts[1] == "of":
            vertex_name = parts[2]
            graph_name = parts[4]
            degree = self.graphs[graph_name].degree(vertex_name)
            print(f"Degree of {vertex_name} in {graph_name}: {degree}")
        elif parts[0] == "all" and parts[1] == "vertices" and parts[2] == "in":
            graph_name = parts[3]
            vertices = self.graphs[graph_name].all_vertices()
            print(f"All vertices in {graph_name}: {vertices}")
        else:
            print("Invalid command")
