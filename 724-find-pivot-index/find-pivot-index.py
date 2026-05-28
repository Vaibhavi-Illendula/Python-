class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls=0
        ts=sum(nums)
        for i in range(len(nums)):
            rs=ts-nums[i]-ls
            if ls==rs:
                return i
            ls+=nums[i]
        return -1
        

        
        