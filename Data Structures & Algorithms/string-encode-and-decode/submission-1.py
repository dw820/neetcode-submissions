class Solution:

    def encode(self, strs: List[str]) -> str:
        encodelist = []

        for string in strs:
            n = len(string)
            encodelist.append(str(n) + '#' + string)

        return ''.join(encodelist)

    def decode(self, s: str) -> List[str]:

        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            ans.append(s[i:j])
            i = j
            
        
        return ans

