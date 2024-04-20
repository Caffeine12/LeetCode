class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # Declaring an empty dictionary of stone counts
        stone_counts = {}
        #Making the keys form the jewels String
        for stone in jewels:
            stone_counts[stone] = 0
        #Count will count the number of jewels present in stones string
        count = 0
        #Matching keys with the values in stones string and increasing number of jewels with count variable
        for stone in stones:
            if stone in stone_counts:
                count+=1
        return count
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        