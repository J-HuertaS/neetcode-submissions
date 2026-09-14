class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        # construir grafo
        for edge in edges:
            graph.setdefault(edge[0],set()).add(edge[1])
            graph.setdefault(edge[1],set()).add(edge[0])

        def dfs(visited, graph, node):
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in graph[node]:
                dfs(visited, graph, neighbor)
            return 1

        output = 0
        visited = set()

        for i in range(n):
            if i in graph:
                output += dfs(visited,graph,i)
            else:
                output += 1

        return output





        