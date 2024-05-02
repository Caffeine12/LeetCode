class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        incoming_edge_set = set()
        smallest_set_of_vertices = []

        for u,v in edges:
            if v not in incoming_edge_set:
                incoming_edge_set.add(v)
        
        for i in range(0,n):
            if i not in incoming_edge_set:
                smallest_set_of_vertices.append(i)
        return smallest_set_of_vertices
    
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """