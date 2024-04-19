class Solution(object):
    def isPowerOfFour(self, n):
        if n>0:
            if n==1:
                return True
            elif n==0:
                return False
            else:
                if n%4 == 0:
                    return self.isPowerOfFour(n/4)
                else:
                    return False
        else:
            return False


        """
        :type n: int
        :rtype: bool
        """
        