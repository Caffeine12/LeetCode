class Solution(object):
    def findJudge(self, n, trust):
        trust_dict = {}
        indegree = 0
        outdegree = 0
        if n==1:
            return 1
        else: 
            for i in range(0,len(trust)):

                if trust[i][0] in trust_dict:
                    trust_dict[trust[i][0]][1]+=1
                else:
                    trust_dict.setdefault(trust[i][0],[indegree,outdegree+1])
                
                if trust[i][1] in trust_dict:
                    trust_dict[trust[i][1]][0]+=1
                else:
                    trust_dict.setdefault(trust[i][1],[indegree+1,outdegree])

            for key in trust_dict:
                if trust_dict[key][0] == n-1 and trust_dict[key][1]==0:
                    return key
            return -1

        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
