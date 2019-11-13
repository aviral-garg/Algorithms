from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def bfs(self, source):
        n = len(self.adj_list)

        if source is None:
            return []

        visited = [False] * n
        result = []

        q = deque([source])
        visited[source] = True
        while q:
            node = q.popleft()
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    result.append(neighbor)
                    q.append(neighbor)
                    visited[neighbor] = True

        print(result)  # or return


# Driver code

if __name__ == '__main__':
    # Create a graph given in this diagram https://imgur.com/RWWEdCj
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.bfs(2)
