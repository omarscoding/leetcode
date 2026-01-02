class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)


# Intial

# for i in nums:
#    if nums.count(i) > 1:
#       return i

# Issue
# The initial implementation using nums.count(i) has a time complexity of O(n^2)
# because for each element in the list, it counts its occurrences in the entire list.
# This can lead to time limit exceeded errors for large inputs.

# Improved
# The improved implementation uses a set to track seen elements.
# This reduces the time complexity to O(n) since checking membership in a set
# and adding elements to a set both have average time complexity of O(1).
# This makes the solution much more efficient for larger input sizes.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Notes
# Sets are a useful data structure for tracking unique elements