from collections import defaultdict
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        smallerNumber_dict = defaultdict(int)
        count = 0
        #creating keys from the list
        for num in nums:
            smallerNumber_dict[num]=0
        #Checking all values with the keys and updating the number of smaller values than the keys
        for num in nums:
            for key in smallerNumber_dict.keys():
                if num<key:
                    smallerNumber_dict[key]+=1
        #Making the list of number of smaller values than the positional value of given list
        return_list = []           
        for i in range(0,len(nums)):
            return_list.append(smallerNumber_dict[nums[i]]) 
        return return_list
    
        """
        :type nums: List[int]
        :rtype: List[int]
        """