from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

    def print_graph(self):
        print("Graph adjacency list:")
        for node in self.adj:
            print(f"  {node} -> {', '.join(str(n) for n in self.adj[node])}")

    def dfs(self, start):
        visited = set()
        stack = [(start, 0)]

        print(f"\nStarting DFS from: {start}")
        while stack:
            node, depth = stack.pop()
            if node not in visited:
                print("  " * depth + node)
                visited.add(node)

                for neighbor in reversed(self.adj.get(node, [])):
                    if neighbor not in visited:
                        stack.append((neighbor, depth + 1))

    def bfs(self, start):
        visited = set()
        queue = deque()

        # enqueue the start node here
        print(f"\nStarting BFS from: {start}")
        while queue:
            pass
            # dequeue a node and its depth
            # if node is not visited:
            # mark as visited
            # print node with indentation
            # enqueue all unvisited neighbors with depth + 1


g = Graph()
g.add_edge("A", "B")
g.add_edge("B", "C")  # same lvl with W
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "F")
g.add_edge("F", "B")  # this forms a cycle
g.add_edge("A", "W")  # same lvl with B
g.add_edge("A", "F")  # this forms a cycle
g.print_graph()
g.dfs("A")
