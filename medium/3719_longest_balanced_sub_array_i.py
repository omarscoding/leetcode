class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0

        for i in range(len(nums)):
            odd = {}
            even = {}

            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even[nums[j]] = even.get(nums[j], 0) + 1
                else :
                    odd[nums[j]] = odd.get(nums[j], 0) + 1
            
                if len(odd) == len(even):
                    max_len = max(max_len, j - i + 1)
        
        return max_len