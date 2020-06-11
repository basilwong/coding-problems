class Solution:

    def create_graph(self, connections):
        for edge in connections:
            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])

    def dfs(self, node, parent):
        # If visited is true then order and low values are set.
        self.visited[node] = True
        self.order[node] = self.counter
        self.low[node] = self.counter
        self.counter += 1

        for child in self.graph[node]:
            if child == parent:
                continue
            elif self.visited[child]:
                self.low[node] = min(self.low[node], self.low[child])
            else:
                self.dfs(child, node)
                self.low[node] = min(self.low[node], self.low[child])
                if self.order[node] < self.low[child]:
                    self.bridges.append([node, child])


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        if n <= 1 or not connections:
            return list()

        self.graph = [set() for _ in range(n)]
        self.bridges = list()
        self.visited = [False] * n
        self.order = [None] * n
        self.low = [-1] * n
        self.counter = 0
        self.create_graph(connections)
        for i in range(n):
            self.dfs(i, -1)

        return self.bridges
