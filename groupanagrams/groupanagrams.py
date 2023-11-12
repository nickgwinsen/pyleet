class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        #sort strings
        srt = [''.join(sorted(i)) for i in strs] #parallel array with sorted strings

        myMap = {} #create map. map structure will be sorted string -> real word real word real
        ans = []
        #iterate base strs
        for x in range(len(strs)): #iterate over the sorted strings
            if srt[x] in myMap: #if the sorted string is in the map,
                myMap[srt[x]].append(strs[x]) #then we will append the corresponding string to the value list
            else:
                myMap[srt[x]] = [] #create value array
                myMap[srt[x]].append(strs[x]) #then add the string that's in that position
        for x in myMap.values():
            ans.append(x) #create answer lists
        return ans #done