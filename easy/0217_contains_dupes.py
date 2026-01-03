class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums :
            if i in seen :
                return True
            seen.add(i)
        return False
    

# Example usage:
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False

# Notes
# Use of sets for efficient tracking of seen elements
# Time Complexity: O(n)
# Space Complexity: O(n)
