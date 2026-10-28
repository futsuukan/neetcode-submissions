class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        containsDuplicate = False
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            try:
                if sorted_nums[i] == sorted_nums[i+1]:
                    containsDuplicate = True
            except:
                print("index out of range")
        return containsDuplicate