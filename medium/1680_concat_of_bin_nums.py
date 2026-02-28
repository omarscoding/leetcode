class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = []

        for i in range(1,n + 1):
            result.append(bin(i)[2:])
        
        ans = ''.join(result)

        return int(ans, 2) % (10**9 + 7)