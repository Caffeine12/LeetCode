class Solution(object):
    def isPowerOfTwo(self, n):
        if n>0:
            while n%2==0:
                n//=2
            return n==1
        return 0
        """
        :type n: int
        :rtype: bool
        """
        