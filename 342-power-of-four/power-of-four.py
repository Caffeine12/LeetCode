class Solution(object):
    def isPowerOfFour(self, n):
        if n>0:
            while n%4==0:
                n//=4
            return n==1
        return 0


        """
        :type n: int
        :rtype: bool
        """
        