class Solution:

    def encode(self, strs: List[str]) -> str:
        encodelist = []

        for string in strs:
            n = len(string)
            encodelist.append(str(n) + '#' + string)

        return ''.join(encodelist)

    def decode(self, s: str) -> List[str]:

        ans = []
        length = ''
        i = 0

        while i < len(s):
            c = s[i]

            if c == '#':
                l = int(length)
                length = ''
                tmp = ''
                for _ in range(l):
                    i+=1
                    tmp += s[i]
                ans.append(tmp)
            else:
                length+=c
            

            i+=1
        
        return ans

