class Solution(object):
    def fib(self, n):
        if n == 0 or n==1:
            return n
        else:
            value = self.fib(n-1) + self.fib(n-2)
            return value

        