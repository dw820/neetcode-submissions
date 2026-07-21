class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_counter = defaultdict(int)
        
        for c in s:
            s_counter[c] += 1

        for c in t:
            if c not in s_counter:
                return False
            
            s_counter[c] -= 1

            if s_counter[c] == 0:
                s_counter.pop(c, None)
        
        return not s_counter
