class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)

        for n in nums:
            if n - 1 not in hashset:
                i = 0
                while n + i in hashset:
                    i += 1
                    if i > res:
                        res = i


        return res