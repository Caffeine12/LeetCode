from collections import defaultdict
class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        list_return = []
        list_edges = [False]*n
        dict_edges = {}
        for u,v in edges:

            if list_edges[u-1] is True and list_edges[v-1]==True:
                if check_loop(u,v,dict_edges):
                    list_return=[u,v]
            else:
                list_edges[u-1] = True
                list_edges[v-1] = True

            if u in dict_edges.keys():
                dict_edges[u].append(v)
            else:
                dict_edges.setdefault(u,[v])
            
            if v in dict_edges.keys():
                dict_edges[v].append(u)
            else:
                dict_edges.setdefault(v,[u])

        return list_return

def check_loop(u,v,dict_edges):
        stack_n = []
        visited = set()
        stack_n.append(u)
        while len(stack_n)>0:
            current = stack_n.pop()
            visited.add(current)
            if current == v:
                return True
            for neighbours in dict_edges[current]:
                if neighbours not in visited:
                    stack_n.append(neighbours)
        return False

        
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """