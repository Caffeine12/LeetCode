class Solution(object):
    def maxDepth(self, s):
        depth = 0
        max_depth = 0
        s_stack = []
        #Finding Max depth
        for i in range(0,len(s)):
            if s[i]=='(':
                s_stack.append(s[i])
                depth+=1
                #Updating Max depth
                if max_depth<depth:
                    max_depth = depth
            elif s[i] == ')':
                s_stack.pop()
                depth-=1
        return max_depth
        """
        :type s: str
        :rtype: int
        """
        