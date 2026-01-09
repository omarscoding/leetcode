class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if max(nums2) < 0 and min(nums1) > 0:
            return max(nums2) * min(nums1)

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + dp[i + 1][j + 1]
                dp[i][j] = max (use, dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


# Example usage:
solution = Solution()
print(solution.maxDotProduct([2,1,-2,5], [3,0,-6]))
# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18

# Notes
# This problem sucks 
# Reminder to add notes later Jan 8th