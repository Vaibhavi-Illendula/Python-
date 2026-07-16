class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # nums = list(set(nums))
        nums.sort()
        max_len = 1
        current_len = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1
        return max(max_len, current_len)
    