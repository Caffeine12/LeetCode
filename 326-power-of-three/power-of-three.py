class Solution(object):
    def isPowerOfThree(self, n):
        if n>0:
            while n%3==0:
                n//=3
            return n==1
        return 0
        """
        :type n: int
        :rtype: bool
        """
        