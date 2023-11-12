class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myMap = {}
        for x in range(len(nums)):
            if nums[x] in myMap:
                myMap[nums[x]] += 1
            else:
                myMap[nums[x]] = 1
        for val in myMap.values():
            if val > 1:
                return True
        return False
            
        