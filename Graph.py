class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
            self.vertices[to_vertex].append(from_vertex)
    
    def neighbors(self, vertex):
        return self.vertices.get(vertex, [])
    
    def is_connected(self, from_vertex, to_vertex):
        visited = set()
        return self._dfs(from_vertex, to_vertex, visited)
    
    def _dfs(self, current, target, visited):
        if current == target:
            return True
        visited.add(current)
        for neighbor in self.vertices.get(current, []):
            if neighbor not in visited:
                if self._dfs(neighbor, target, visited):
                    return True
        return False
    
    def is_empty(self):
        return len(self.vertices) == 0
    
    def degree(self, vertex):
        return len(self.vertices.get(vertex, []))
    
    def all_vertices(self):
        return list(self.vertices.keys())
