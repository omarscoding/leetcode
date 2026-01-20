class Solution(object):
    def minBitwiseArray(self, nums):
        for i in range(len(nums)) :
            res = -1
            bit = 1
            while (nums[i] & bit) != 0 :
                res = nums[i] - bit
                bit <<= 1
            nums[i] = res
        return nums