class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for n, m in enumerate(nums):
            if n > 0 and m == nums[n - 1]:
                continue

            i = n + 1
            j = len(nums) - 1
            while i < j:
                if (m + nums[i] + nums[j]) > 0:
                    j -= 1
                elif (m + nums[i] + nums[j]) < 0:
                    i += 1
                else:
                    res.append([m, nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
        return res