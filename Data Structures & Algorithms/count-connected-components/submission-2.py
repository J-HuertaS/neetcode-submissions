class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        # construir grafo
        for edge in edges:
            graph.setdefault(edge[0],set()).add(edge[1])
            graph.setdefault(edge[1],set()).add(edge[0])

        def dfs(visited, graph, node, parent):
            if node in visited:
                return 0

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(visited,graph,neighbor,node)

            return 1

        output = 0
        visited = set()

        for i in range(n):
            if i in graph:
                output += dfs(visited,graph,i,None)
            else:
                output += 1

        return output





        