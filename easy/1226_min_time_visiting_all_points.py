class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        ans = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            targ_x, targ_y = points[i + 1]
            ans += max(abs(targ_x - curr_x), abs(targ_y - curr_y))
        return ans
    
# Example usage:
solution = Solution()
points = [[1,1],[3,4],[-1,0]]
print(solution.minTimeToVisitAllPoints(points))  # Output: 7

# Notes:
# The minimum time to visit all points is calculated by summing the maximum of the absolute differences
# in the x and y coordinates between each consecutive pair of points.

# Time Complexity: O(N), where N is the number of points.
# Space Complexity: O(1), as we are using only a constant amount of extra space.

# Personal thoughts:
# I love leetcode easy

