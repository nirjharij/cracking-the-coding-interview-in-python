import random


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.temp_dict = {}
        self.visited = set()
        self.cycle_found = False
        unique_courses = set()

        if not prerequisites:
            return True
        for item in prerequisites:
            src = item[0]
            dest = item[1]
            unique_courses.add(src)
            unique_courses.add(dest)
            if src not in self.temp_dict:
                self.temp_dict[src] = [dest]
            else:
                self.temp_dict[src].append(dest)

        while len(self.visited) != len(unique_courses):
            n = random.randint(0, len(prerequisites) - 1)
            src = prerequisites[n][0]
            if src in self.visited:
                continue
            self.visited.add(src)
            self.dfs(src)
            if self.cycle_found:
                break

        if self.cycle_found:
            return False
        return True

    def dfs(self, node, src_list=[]):
        if node in self.temp_dict:
            src_list.append(node)
            for i in range(len(self.temp_dict[node])):
                current_node = self.temp_dict[node][i]
                if current_node in self.visited and current_node in src_list:
                    self.cycle_found = True
                    return
                elif current_node in self.visited:
                    continue
                self.visited.add(current_node)
                self.dfs(current_node, src_list)
