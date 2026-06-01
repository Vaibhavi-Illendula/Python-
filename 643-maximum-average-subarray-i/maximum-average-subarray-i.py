class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_s = sum(nums[:k])
        max_sum = w_s
        for i in range(k, len(nums)):
            w_s += nums[i] - nums[i - k]
            max_sum = max(max_sum, w_s)

        return max_sum / k
        
        