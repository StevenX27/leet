# backtrack
class Solution:
    def permute(self, nums):
        
        n = len(nums)
        arr = []

        def backtrack(index):
            if(index == n):
                arr.append(nums[:])
                return
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index] # swap
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index] # swap back
        
        backtrack(0)
        print(arr)
        return arr
    
Sol= Solution()
Sol.permute([1,2])