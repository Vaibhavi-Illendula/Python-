class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # # nums = list(set(nums))
        # nums.sort()
        # max_len = 1
        # current_len = 1
        # for i in range(1, len(nums)):
        #     if nums[i]==nums[i-1]:
        #         continue
        #     if nums[i] == nums[i-1] + 1:
        #         current_len += 1
        #     else:
        #         max_len = max(max_len, current_len)
        #         current_len = 1
        # return max(max_len, current_len)
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:   
                current = num
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
    