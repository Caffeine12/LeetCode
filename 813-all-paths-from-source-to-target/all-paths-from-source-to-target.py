class Solution(object):
    def allPathsSourceTarget(self, graph):
        res = []
        n = len(graph)
        stack_dfs = [(0,[0])]
        while(len(stack_dfs)>0):
            node,path = stack_dfs.pop()
            if node == (n-1):
                res.append(path)
            for neighbour in graph[node]:
                stack_dfs.append((neighbour,path+[neighbour]))
        return res
        
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """




        