from collections import defaultdict
class Solution(object):
    def numIdenticalPairs(self, nums):
        goodPair_dict = defaultdict(list)
        key_numbers = []

        # Making the hash table for same integers
        for i,number in enumerate(nums):
            key_numbers = number
            goodPair_dict[key_numbers].append(i)
        
        # Counting the number of good pairs
        count = 0
        for value in goodPair_dict.values():
            for i in range(1,len(value)):
                count = count+(len(value)-i)
        return count

        """
        :type nums: List[int]
        :rtype: int
        """
        