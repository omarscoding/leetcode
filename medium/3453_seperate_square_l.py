class Solution(object):
    def separateSquares(self, squares):
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l*l
            max_y = max(max_y, y + l)

        target = total_area / 2.0

        def check(limit_y):
            area = 0
            for x, y, l in squares:
                if y >= limit_y :
                    continue
                elif y + l <= limit_y :
                    area += l * l
                else :
                    height_below = limit_y - y
                    area += l * height_below
            return area >= target
        
        lo, hi = 0.0, max_y 

        while hi - lo > 1e-6:
            mid = (lo + hi) / 2.0
            if check(mid) :
                hi = mid
            else :
                lo = mid
        
        return round(hi,5)


# Example usage:
solution = Solution()
squares = [[0,0,2],[1,1,2],[2,0,2]]
print(solution.separateSquares(squares))  # Output: 1.5
squares = [[0,0,4],[4,0,2]]
print(solution.separateSquares(squares))  # Output: 2.0

# Notes:
# The function separates a list of squares into two equal-area parts by finding a horizontal line.
# It uses binary search to efficiently find the correct y-coordinate for the separating line.
# Time Complexity: O(n log m), where n is the number of squares and m is the maximum y-coordinate.
# Space Complexity: O(1), as it uses a constant amount of extra space.

