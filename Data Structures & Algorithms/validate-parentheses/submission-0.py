class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for c in s:
            if c in mapping:
                if not stack:
                    return False

                last = stack.pop()
                if last != mapping[c]:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
                