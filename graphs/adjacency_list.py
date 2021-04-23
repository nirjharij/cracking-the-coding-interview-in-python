class AdjacentNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self, src, dest):
        node = AdjacentNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        node = AdjacentNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def dfs(self, v):
        visited = [False] * self.vertices
        self.dfs_util(v, visited)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def bfs(self, num):
        visited = [False] * self.vertices

        queue = list()
        queue.append(num)
        visited[num] = True

        while queue:
            item = queue.pop(0)
            print(item)
            for i in self.graph[item]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()
