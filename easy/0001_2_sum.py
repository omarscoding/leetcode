class Solution(object):
    def twoSum(self, nums, target):
        has = {}
        for i in range(len(nums)) :
            has[nums[i]] = i 
        
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in has and has[compl] != i :
                return [i, has[compl]]

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]

# Time Complexity: O(n), where n is the number of elements in the nums list.
# Space Complexity: O(n), as we are using a hash map to store the elements of nums.

# Notes
# The two-sum problem is a classic algorithmic problem that can be efficiently solved using a hash map (dictionary in Python). 
# The idea is to store each number in the hash map along with its index as we iterate through the list. For each number, 
# we calculate its complement (the number that, when added to the current number, equals the target). We then check if this complement exists in the hash map.
# If it does, we have found the two numbers that add up to the target, and we return their indices. 
# This approach allows us to find the solution in a single pass through the list, resulting in a time complexity of O(n).

