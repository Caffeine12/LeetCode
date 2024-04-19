import math
class Solution(object):
    def isPowerOfFour(self, n):
        if n > 0:
            x = math.log(n,4)
            if(x.is_integer()):
                return True
            else:
                return False
        else:
            return False

        """
        :type n: int
        :rtype: bool
        """
        