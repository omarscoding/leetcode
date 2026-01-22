class Solution(object):
    def minimumPairRemoval(self, nums):
        count = 0

        def is_sorted(arr) :
            for i in range(len(arr) - 1) :
                if arr[i] > arr[i + 1] :
                    return False
            return True


        while not is_sorted(nums) :
            min_sum = float('inf')
            min_index = 0

            for i in range(len(nums) - 1) :
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i

            nums[min_index] = min_sum
            nums.pop(min_index + 1)
            count += 1
        
        return count