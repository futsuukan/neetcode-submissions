class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        hashset = set()

        for j in range(len(s)):
            while s[j] in hashset:
                hashset.remove(s[i])
                i += 1
            hashset.add(s[j])
            res = max(j - i + 1, res)
        
        return res