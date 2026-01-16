class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])

        best = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in h_dist:
                    if d > best:
                        best = d

        if best == -1:
            return -1

        return (best * best) % MOD