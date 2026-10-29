class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        brackets = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in brackets:
                if res and res[-1] == brackets[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        
        return True if not res else False