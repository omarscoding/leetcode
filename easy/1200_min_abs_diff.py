class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        n = len(arr)
        minDiff = arr[n-1] - arr[n-2]
        for i in range(1, n):
            minDiff = min(minDiff, arr[i] - arr[i-1])
        ans = []
        for i in range(1, n):
            if arr[i] - arr[i-1] == minDiff:
                ans.append([arr[i-1], arr[i]])
        return ans
        