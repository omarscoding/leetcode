class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
        
# Intial

#   length = len(digits)
#         if digits[length-1] < 9:
#             digits[length-1] += 1
#         else:
#             digits.append(0)
#         return digits

# Issue
# The initial implementation only checks the last digit and does not handle cases
# where there are multiple digits that need to be incremented (e.g., carrying over).
# For example, if the input is [9, 9], the expected output is [1, 0, 0],
# but the initial code would return [9, 0], which is incorrect.

# Improved
# The improved implementation iterates through the digits from the last to the first.
# It checks if the current digit is less than 9; if so, it increments that digit and returns the list.
# If the digit is 9, it sets it to 0 and continues to the next digit.
# If all digits are 9, it prepends a 1 to the list (e.g., [9, 9] becomes [1, 0, 0]).
# This approach correctly handles carrying over for multiple digits.
# Time Complexity: O(n) in the worst case when all digits are 9.
# Space Complexity: O(1) if we don't count the output list, otherwise O(n) when a new digit is added.

# Notes
# for i in range(len(digits) - 1, -1, -1):
# This loop iterates through the list of digits in reverse order,
# allowing us to handle the least significant digit first,
# which is essential for correctly implementing the "plus one" logic with carrying over.

# Example usage:
solution = Solution()
print(solution.plusOne([9, 9]))
# Input: digits = [9, 9]