class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        myMap = {}
        ans = []
        for x in nums:
            if x in myMap:
                myMap[x] += 1
            else:
                myMap[x] = 1
        #frequency is done
        for x in range(k):
            #we go k times
            maxVal = 0
            maxKey = 0
            for y in myMap:
                #now we find max value
                if myMap[y] > maxVal:
                    maxKey = y
                    maxVal = myMap[y] #store key in maxVal and also pop
            myMap.pop(maxKey)
            ans.append(maxKey)
        return ans
