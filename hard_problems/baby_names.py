from collections import defaultdict

names_dict = {'John': 15, 'Jon': 12, 'Chris': 13, 'Kris': 4, 'Christopher': 19}
final_dict = defaultdict(lambda: 0)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
        if a not in self.visited:
            self.visited[a] = False
        if b not in self.visited:
            self.visited[b] = False

    def dfs(self, name, main_name):
        self.visited[name] = True
        if name in names_dict:
            freq = names_dict[name]
            final_dict[main_name] += freq

        for item in self.graph[name]:
            if not self.visited[item]:
                self.dfs(item, main_name)


g = Graph()
g.add_edge('Jon', 'John')
g.add_edge('John', 'Johnny')
g.add_edge('Chris', 'Kris')
g.add_edge('Chris', 'Christopher')
for item in g.graph:
    if g.visited[item]:
        continue
    final_dict[item] = 0
    g.dfs(item, item)

print(final_dict)
