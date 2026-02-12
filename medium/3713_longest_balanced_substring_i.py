class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            cnt ={}

            for j in range(i, n):
                cnt[s[j]] = cnt.get(s[j], 0) + 1

                num_distinct = len(cnt)
                max_freq = max(cnt.values())

                if max_freq * num_distinct == (j - i + 1):
                    ans = max(ans, j - i + 1)

        return ans