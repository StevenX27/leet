class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        
        for i in range(len(nums)):
            if nums[i] not in frequency:
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] += 1
        
        for key in frequency:
            if frequency[key] == 1:
                print(key)
                return key
            
sol = Solution()
sol.singleNumber([0,1,0,1,0,1,99])