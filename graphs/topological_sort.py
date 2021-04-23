class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.child = None


class Graph:
    def __init__(self, *projects):
        self.visited = dict()
        self.graph = dict()
        self.final_output = list()
        for project in projects:
            self.graph[project] = list()
            self.visited[project] = False

    def add_edge(self, src, dest):
        new_node = Node(src)
        self.graph[dest].append(new_node)

    def print_graph(self):
        # print(self.graph)
        print(self.final_output)

    def topological_sort(self):
        while not all(list(self.visited.values())):
            for i, j in self.graph.items():
                if not self.visited[i]:
                    node = self.graph[i]
                    src = i
                    self.visited[i] = True
                    if not node:
                        if i not in self.final_output:
                            self.final_output.append(i)
                    break
            self.dfs(node)
            if src not in self.final_output:
                self.final_output.append(src)

    def dfs(self, node):
        for n in node:
            if self.graph[n.vertex] and not self.visited[n.vertex]:
                self.visited[n.vertex] = True
                self.dfs(self.graph[n.vertex])
            self.visited[n.vertex] = True
            if n.vertex not in self.final_output:
                self.final_output.append(n.vertex)


if __name__ == "__main__":
    graph_obj = Graph("a", "b", "c", "d", "e", "f")
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    for dependency in dependencies:
        graph_obj.add_edge(dependency[0], dependency[1])
    graph_obj.topological_sort()
    graph_obj.print_graph()
