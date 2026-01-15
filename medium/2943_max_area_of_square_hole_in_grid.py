class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def longest_consecutive(arr):
            arr.sort()
            longest = cur = 1
            for i in range(1, len(arr)):
                cur = cur + 1 if arr[i] == arr[i - 1] + 1 else 1
                longest = max(longest, cur)
            return longest

        side = min(longest_consecutive(hBars),
                   longest_consecutive(vBars)) + 1
        return side * side