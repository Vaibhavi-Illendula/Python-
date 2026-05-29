class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        c_s=0
        for i in nums:
            c_s+=i
            self.prefix.append(c_s)
    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.prefix[right]-self.prefix[left-1]
        else:
            return self.prefix[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)