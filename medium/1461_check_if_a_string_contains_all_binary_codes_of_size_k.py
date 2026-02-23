class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        target = 2**k

        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
            if len(seen) == target:
                return True

        return len(seen) == target