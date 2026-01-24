class Solution(object):
    def minPairSum(self, nums):
        ans = 0
        nums = sorted(nums)

        start = 0
        end = len(nums) - 1
    
        while start < end :
            ans = max(ans, nums[start] + nums[end])
            start += 1
            end -= 1

        return ans