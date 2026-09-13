class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        # construir grafo
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        # construir check
        check = [0 for _ in range(numCourses)]

        def dfs(numCourses, graph, node, path, check):
            if node in path:
                return False

            if check[node]:
                return True

            path.add(node)

            # busca en los demas
            for i in graph[node]:
                if not dfs(numCourses, graph, i, path, check):
                    return False

            path.remove(node)

            check[node] = 1

            return True

        for i in range(numCourses):
            path = set()
            if not dfs(numCourses, graph, i, path, check):
                return False

        return True