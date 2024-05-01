import collections
class Solution:
    def validPath(self, n, edges, source, destination):

        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
        return dfs(source)
        
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """