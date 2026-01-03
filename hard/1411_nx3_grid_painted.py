class Solution(object):
    def numOfWays(self, n):
        mod = 10**9 + 7

        # Patterns count, for n = 1
        aba = 6  # Patterns like RGR
        abc = 6  # Patterns like RGY

        # Iterate from row 2 to row n
        for i in range(n-1):
            next_aba = (3 * aba + 2 * abc) % mod
            next_abc = (2 * aba + 2 * abc) % mod 

            aba = next_aba
            abc = next_abc

        return (aba + abc) % mod
    
# Notes
# Wasn't able to solve on my own
# https://www.youtube.com/watch?v=W-WvItFiWX8
# Explanation of the approach:
# The problem can be solved using dynamic programming by recognizing the patterns in painting the grid.
# We can categorize the ways to paint each row into two types of patterns:
# 1. "aba" patterns: These are patterns where the first and third columns have the same color,
#    and the second column has a different color (e.g., RGR, YGY).
# 2. "abc" patterns: These are patterns where all three columns have different colors (e.g., RGY, RYG).
# For each row, the number of ways to paint it depends on the pattern of the previous row:
# - If the previous row is an "aba" pattern, the current row can be painted in:
#   - 3 ways to form another "aba" pattern (e.g. RGR -> GRG | RGR -> GYG | RGR -> YRY)
#   - 2 ways to form an "abc" pattern (e.g. RGR -> YRG | RGR -> GRY) (Middle column must be from the previous A)
# - If the previous row is an "abc" pattern, the current row can be painted in:
#   - 2 ways to form an "aba" pattern (e.g. RGY -> GRG | RGY -> GYG) (First and last column must be from the previous B)
#   - 2 ways to form another "abc" pattern (e.g. RGY -> YRG | RGY -> GYR)
# We can use two variables, `aba` and `abc`, to keep track of the number of ways to paint the grid
# for each pattern type as we iterate through each row from 2 to n.
# Finally, the total number of ways to paint the grid is the sum of the ways to paint it
# using both pattern types, modulo 10^9 + 7.

# Example usage:
solution = Solution()
print(solution.numOfWays(3))
# Input: n = 3
# Output: 246
# Explanation: There are 246 ways to paint a 3 x 3 grid such that no two adjacent cells have the same color.

# Personal Thoughts
# At first, i found this question to be quite difficult to comprehend
# however, after understadning the patterns that must be followed depending on the previous row
# it became much more clear on how to approach the problem
# And had become a simple matter of counting the patterns and using dynamic programming (breaking down the problem, into smaller subproblems) 
# to store the results 
# Drawing out the problem and the different combinations made it much easier to understand what i was supposed to be doing
# and how i should be thinking and approaching the problem
