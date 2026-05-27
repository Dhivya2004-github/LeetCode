class Solution(object):
    def countTrapezoids(self, points):
        from collections import defaultdict
        
        MOD = 10**9 + 7
        
        rows = defaultdict(int)
        for x, y in points:
            rows[y] += 1
        
        segs = []
        for k in rows.values():
            if k >= 2:
                segs.append(k * (k - 1) // 2)
        
        S = sum(segs) % MOD
        sumsq = sum((x * x) % MOD for x in segs) % MOD
        
        ans = (S * S - sumsq) % MOD
        ans = ans * pow(2, MOD - 2, MOD) % MOD  
        return ans % MOD