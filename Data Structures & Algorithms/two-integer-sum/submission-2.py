class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()

        for n in nums:
            hashset.add(n)

        for i in range(len(nums)):
            number = target - nums[i]
            if number in hashset and nums.index(number) != i:
                return sorted([nums.index(number), i])