from collections import defaultdict
class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        city_stack = []
        visited = set()
        province = 0
        for r in range(0,n):
            for c in range(r,n):
                if (r,c) not in visited and isConnected[r][c] == 1:
                    if r==c:
                        province +=1
                    else:                        
                        city_stack.append(c)
                    
                    visited.add((r,c))
                    visited.add((c,r))
                    
                    while(len(city_stack)>0):
                        current = city_stack.pop()
                        for neighbour in range(0,n):
                            if current!= neighbour and (current,neighbour) not in visited and isConnected[current][neighbour]==1:
                                visited.add((current,neighbour))
                                visited.add((neighbour,current))
                                city_stack.append(neighbour)
                            elif current==neighbour:
                                visited.add((current,neighbour))
        return province
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        