class Solution(object):
    def lengthOfLastWord(self, s):
        parts = s.strip().split(" ")
        return len(parts[-1])


        
        """
        :type s: str
        :rtype: int
        """
        