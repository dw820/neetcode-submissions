class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        def hash(s):
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            arr_s = [str(a) for a in arr]
            return '-'.join(arr_s)
        
        mapping = defaultdict(list)

        for string in strs:
            h = hash(string)
            
            mapping[h].append(string)

        ans = []

        for value in mapping.values():
            ans.append(value)
        
        return ans

            
