class Solution(object):
    def sumFourDivisors(self, nums):
        total = 0
        for i in nums:
            seen = set()
            for n in range(1, int(i**0.5) + 1) :
                if i % n == 0:
                    seen.add(n)
                    seen.add(i // n)
                if len(seen) > 4 :
                    break

            if len(seen) == 4 :
                total += sum(seen)
        return total        


# Initial

# class Solution(object):
#     def sumFourDivisors(self, nums):
#         total = 0
#         for i in nums:
#             seen = set()
#             for n in range(1, int(i**0.5) + 1) :
#                 if i % n == 0:
#                     seen.add(n)
#                     seen.add(i // n)
#             if len(seen) == 4 :
#                 total += sum(seen)
#         return total        

# Issue
# The initial implementation checks all possible divisors for each number in nums,
# which can be inefficient for larger numbers. The time complexity is O(n * sqrt(m)),
# where n is the length of nums and m is the maximum number in nums.

# Improved
# The improved implementation includes an early exit condition.
# If at any point the number of divisors found exceeds 4, we break out of the loop early.
# This optimization reduces unnecessary computations for numbers that have more than 4 divisors.
# Time Complexity: O(n * sqrt(m)) in the worst case, but often better due to early exit.
# Space Complexity: O(1) additional space, since the size of the seen set is at most 4.

# Example usage:
solution = Solution()
print(solution.sumFourDivisors([21, 4, 7]))  # Output: 32
# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The only number with exactly 4 divisors is 21. So the answer is 1 + 3 + 7 + 21 = 32.

# Notes
# We use the square root of the number to limit the range of potential divisors,
# since divisors come in pairs (d and n/d).
# By using a set, we ensure that each divisor is only counted once.

# Time Complexity: O(n * sqrt(m)) in the worst case, where n is the length of nums and m is the maximum number in nums.
# Space Complexity: O(1) additional space, since the size of the seen set is at most 4.