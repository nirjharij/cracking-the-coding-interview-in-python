class Graph:
    def __init__(self, vertices):
        self.visited = [[False] * vertices for i in range(vertices)]
        self.adj_matrix = [[-1] * vertices for i in range(vertices)]
        self.vertices = vertices
        self.vertices_dict = {}
        self.vertices_list = [0] * vertices

    def set_vertex(self, vertex, id):
        if 0 <= vertex <= self.vertices:
            self.vertices_dict[id] = vertex
            self.vertices_list[vertex] = id

    def set_edge(self, src, dest, weight):
        src = self.vertices_dict[src]
        dest = self.vertices_dict[dest]
        self.adj_matrix[src][dest] = weight
        self.adj_matrix[dest][src] = weight

    def get_vertex(self):
        return self.vertices_list

    def get_edges(self):
        edges = []
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj_matrix[i][j] != -1:
                    edges.append((self.vertices_list[i], self.vertices_list[j], self.adj_matrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adj_matrix

    def bfs(self):
        queue = list()
        queue.append(self.adj_matrix[0][2])
        self.visited[0][2] = True
        row = 0
        col = 2
        while queue:
            print(queue.pop(0))
            directions_row = [row, row + 1, row, row - 1]
            directions_col = [col + 1, col, col - 1, col]
            for item in zip(directions_row, directions_col):
                row = item[0]
                col = item[1]
                if (row >= 0 and row < self.vertices) and (col >= 0 and col < self.vertices):
                    if not self.adj_matrix[row][col] == -1:
                        if not self.visited[row][col]:
                            queue.append(self.adj_matrix[row][col])
                            self.visited[row][col] = True


if __name__ == '__main__':
    G = Graph(6)
    G.set_vertex(0, 'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')
    G.set_vertex(5, 'f')
    G.set_edge('a', 'e', 10)
    G.set_edge('a', 'c', 20)
    G.set_edge('c', 'b', 30)
    G.set_edge('b', 'e', 40)
    G.set_edge('e', 'd', 50)
    G.set_edge('f', 'e', 60)
    # print("Vertices of Graph")
    # print(G.get_vertex())
    # print("Edges of Graph")
    print(G.get_edges())
    # print("Adjacency Matrix of Graph")
    # print(G.get_matrix())
    G.bfs()
