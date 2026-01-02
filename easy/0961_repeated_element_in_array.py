class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)

