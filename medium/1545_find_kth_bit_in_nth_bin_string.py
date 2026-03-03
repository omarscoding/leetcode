class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        length = (1 << n) - 1
        mid = (length // 2) + 1

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirror_k = length - k + 1
            bit = self.findKthBit(n - 1, mirror_k)
            return "1" if bit == "0" else "0"