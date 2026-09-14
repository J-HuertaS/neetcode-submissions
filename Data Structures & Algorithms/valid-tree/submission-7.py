class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        nodes = set()
        # construir grafo
        for pair in edges:
            graph.setdefault(pair[0], set()).add(pair[1])
            graph.setdefault(pair[1], set()).add(pair[0])
            nodes.add(pair[0])
            nodes.add(pair[1])

        def dfs_cycle(graph, node, direct_parent, path, visited):
            path.add(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in path:
                    if neighbor != direct_parent:
                        return True
                else: 
                    if dfs_cycle(graph, neighbor, node, path,visited):
                        return True

            path.remove(node)

            return False


        path = set()
        visited = set()

        if len(nodes):
            return not dfs_cycle(graph,0,None,path,visited) and visited == nodes
        else:
            return True
        